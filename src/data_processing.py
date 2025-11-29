"""
Core Data Processing Functions for FDSE Challenge

CANDIDATE TASK: Implement the three functions below according to their specifications.

These functions form the core of an industrial data processing pipeline.
You will work with real-world challenges like missing data, connection failures,
and noisy sensor readings.

IMPORTANT NOTES:
- Function signatures (names, parameters, return types) must not be changed
- You may add helper functions in this file or create new modules
- Focus on robustness, error handling, and data quality
- Document your assumptions and trade-offs in NOTES.md
- Aim for production-quality code, not just passing tests
"""

from typing import Dict, List, Optional, Tuple
import pandas as pd
import numpy as np


def ingest_data(
    data_batches: List[pd.DataFrame],
    validate: bool = True,
) -> pd.DataFrame:
    """
    Ingest and consolidate multiple batches of industrial sensor data.
    
    This function must handle real-world data quality issues:
    - Missing or null values
    - Duplicate readings
    - Out-of-order timestamps
    - Data from different sensors with different units
    - Potentially empty batches
    
    Args:
        data_batches: List of DataFrames, each with columns:
            - timestamp (datetime): When the reading was taken
            - sensor (str): Sensor identifier (e.g., "temperature", "pressure")
            - value (float): Sensor reading (may be NaN)
            - unit (str): Unit of measurement
            - quality (str): Data quality flag ("GOOD", "BAD", "UNCERTAIN")
        validate: If True, perform data validation and cleanup
    
    Returns:
        Consolidated DataFrame with cleaned, deduplicated, and sorted data.
        Should maintain all original columns plus any derived quality metrics.
    
    Raises:
        ValueError: If data_batches is empty or contains invalid data structures
    
    Example:
        >>> batches = simulator.get_batch_readings(num_batches=5)
        >>> clean_data = ingest_data(batches, validate=True)
        >>> print(f"Ingested {len(clean_data)} readings from {len(batches)} batches")
    
    CANDIDATE TODO:
    - Implement robust data ingestion
    - Handle edge cases (empty batches, all bad quality, etc.)
    - Remove duplicates intelligently
    - Sort by timestamp
    - Consider filtering by quality flags
    - Document your data cleaning strategy in NOTES.md
    """
    
    # data branches empty
    if not data_batches:
        raise ValueError("data_batches list is empty")
    
    # data branches contain invalid data structures
    for b in data_batches:
        if not isinstance(b, pd.DataFrame):
            raise ValueError("Each item in data_batches must be a pandas DataFrame")
        required_columns = {"timestamp", "sensor", "value", "unit", "quality"}
        if not required_columns.issubset(b.columns):
            raise ValueError(f"DataFrame missing required columns: {required_columns}")

    consolidated_df = pd.concat(data_batches, ignore_index=True)

    # data validation and cleanup
    if validate:
        # out-of-order timestamps
        consolidated_df["timestamp"] = pd.to_datetime(consolidated_df["timestamp"])
        data_batches_cleaned = []
        for batch in data_batches:
            # print("\n---- batch", batch)
            # missing or null values
            batch = batch.dropna(subset=["timestamp", "sensor"])
            # fill missing values with NaN
            batch["value"] = batch["value"].astype(float)
            # filter bad quality data
            batch = batch[batch["quality"] != "BAD"]
            
            # remove duplicates
            batch = batch.drop_duplicates(subset=["timestamp", "sensor"])

            batch = batch.sort_values(by="timestamp")
            data_batches_cleaned.append(batch)

        consolidated_df = pd.concat(data_batches_cleaned, ignore_index=True)
        # different sensors with different units
        consolidated_df["value"] = pd.to_numeric(consolidated_df["value"], errors='coerce') 
        consolidated_df = consolidated_df.dropna(subset=["value"])
        consolidated_df = consolidated_df.sort_values(by="timestamp").reset_index(drop=True)

    return consolidated_df


def detect_anomalies(
    data: pd.DataFrame,
    sensor_name: str,
    method: str = "zscore",
    threshold: float = 3.0,
) -> pd.DataFrame:
    """
    Detect anomalies in sensor data using statistical methods.
    
    Industrial sensors can produce anomalous readings due to:
    - Equipment malfunctions
    - Environmental changes
    - Sensor calibration drift
    - Communication errors
    
    Args:
        data: DataFrame from ingest_data() containing sensor readings
        sensor_name: Name of the sensor to analyze (e.g., "temperature")
        method: Detection method - "zscore", "iqr", or "rolling"
            - "zscore": Flag values beyond threshold standard deviations from mean
            - "iqr": Flag values beyond threshold * IQR from quartiles
            - "rolling": Flag based on rolling window statistics
        threshold: Sensitivity parameter (interpretation depends on method)
    
    Returns:
        DataFrame with original data plus new columns:
            - is_anomaly (bool): True if reading is anomalous
            - anomaly_score (float): Numeric score indicating severity
            - detection_method (str): Method used for detection
    
    Raises:
        ValueError: If sensor_name not found or method not supported
        ValueError: If insufficient data for the chosen method
    
    Example:
        >>> anomalies = detect_anomalies(clean_data, "temperature", method="zscore", threshold=3.0)
        >>> num_anomalies = anomalies['is_anomaly'].sum()
        >>> print(f"Found {num_anomalies} anomalies in temperature data")
    
    CANDIDATE TODO:
    - Implement at least the "zscore" method (others are optional but valued)
    - Handle missing values appropriately
    - Consider data quality flags in anomaly detection
    - Return meaningful anomaly scores for ranking/prioritization
    - Think about edge cases: what if all data is anomalous? None is?
    - Document your approach and limitations in NOTES.md
    """
    

    methods_supported = {"zscore", "iqr", "rolling"}
    # method not supported
    if method not in methods_supported:
        raise ValueError(f"Method '{method}' not supported. Choose from {methods_supported}")
    # sensor_name not found
    if sensor_name not in data['sensor'].unique():
        raise ValueError(f"Sensor '{sensor_name}' not found in data")
    


    final_df = data.copy()

    # new columns
    final_df["is_anomaly"] = False
    final_df["anomaly_score"] = 0.0
    final_df["detection_method"] = method

    # zscore
    if method == "zscore":
        # not enough data for the method
        sensor_data = data[data["sensor"] == sensor_name].copy()
        values = sensor_data["value"].dropna()
        std = values.std()
        if len(values) < 2 or pd.isna(std) or std == 0:
            raise ValueError("Insufficient data for zscore method")
        
        mean = values.mean()
        z_scores = (values - mean) / std

        final_df["anomaly_score"] = z_scores
        if (abs(z_scores) > threshold).any():
            final_df["is_anomaly"] = True
        final_df["is_anomaly"] = final_df["is_anomaly"].fillna(False)

    # TODO iqr method
    elif method == "iqr":
        raise NotImplementedError("IQr method not implemented yet")


    # TODO rolling method
    elif method == "rolling":
        raise NotImplementedError("Rolling method not implemented yet")    

    return final_df




def summarize_metrics(
    data: pd.DataFrame,
    group_by: Optional[str] = "sensor",
    time_window: Optional[str] = None,
) -> Dict[str, Dict[str, float]]:
    """
    Generate summary statistics for industrial sensor data.
    
    Summaries help operators and engineers understand system behavior:
    - Overall sensor performance
    - Data quality metrics
    - Temporal patterns
    - Anomaly rates
    
    Args:
        data: DataFrame from ingest_data() or detect_anomalies()
        group_by: Column to group by (typically "sensor")
        time_window: Optional pandas frequency string for time-based aggregation
            Examples: "1h" (hourly), "15min" (15 minutes), "1d" (daily)
            If None, compute overall statistics without time grouping
    
    Returns:
        Nested dictionary structure:
        {
            "sensor_name": {
                "mean": float,
                "std": float,
                "min": float,
                "max": float,
                "count": int,
                "null_count": int,
                "good_quality_pct": float,
                "anomaly_rate": float,  # if anomaly data available
                # ... additional metrics as appropriate
            },
            ...
        }
        
        If time_window is specified, returns time-indexed groups.
    
    Raises:
        ValueError: If group_by column doesn't exist
        ValueError: If data is empty or invalid
    
    Example:
        >>> metrics = summarize_metrics(anomaly_data, group_by="sensor")
        >>> temp_metrics = metrics["temperature"]
        >>> print(f"Temperature: {temp_metrics['mean']:.1f}°C ± {temp_metrics['std']:.1f}")
        >>> print(f"Data quality: {temp_metrics['good_quality_pct']:.1f}% good readings")
    
    CANDIDATE TODO:
    - Compute essential statistics (mean, std, min, max, count)
    - Calculate data quality metrics (null rate, quality flag distribution)
    - If anomaly detection was run, include anomaly statistics
    - Handle time-based grouping if time_window is provided
    - Consider what metrics are most valuable for industrial monitoring
    - Ensure robust handling of edge cases (all nulls, single value, etc.)
    - Document your metric choices in NOTES.md
    """
    
    if data.empty:
        raise ValueError("Input data is empty")
    if group_by and group_by not in data.columns:
        raise ValueError(f"Column '{group_by}' not found in data")
    
    if time_window:
        # set timestamp as index
        if 'timestamp' not in data.columns:
            raise ValueError("Column 'timestamp' not found in data for time-based aggregation")
        
        #check timestamp dtype
        if not pd.api.types.is_datetime64_any_dtype(data["timestamp"]):
            data = data.copy()
            data["timestamp"] = pd.to_datetime(data["timestamp"])

        all_data = data.groupby([group_by, pd.Grouper(key="timestamp", freq=time_window)])
    else:
        all_data = data.groupby(group_by)

    results = {}
    for group_name, group_df in all_data:
        metrics = {}
        values = group_df["value"].dropna()

        metrics = {
            "mean": values.mean(),
            "std": values.std(),
            "min": values.min(),
            "max": values.max(),
            "count": len(values),
            "null_count": group_df["value"].isna().sum()
        }
        # quality metrics
        if "quality" in group_df.columns:
            good_count = (group_df["quality"] == "GOOD").sum()
            metrics["good_quality_pct"] = (good_count / len(group_df)) * 100.0 if len(group_df) > 0 else 0.0
        else:
            metrics["good_quality_pct"] = 0.0

        # anomaly metrics
        if "is_anomaly" in group_df.columns:
            anomaly_count = group_df["is_anomaly"].sum()
            metrics["anomaly_rate"] = (anomaly_count / len(group_df)) if len(group_df) > 0 else 0.0
    
        if time_window:
            sensor = group_name[0]
            time_bucket = group_name[1]
            if sensor not in results:
                results[sensor] = {}
            
            results[sensor][str(time_bucket)] = metrics
            
        else:
            results[group_name] = metrics
    
    return results
