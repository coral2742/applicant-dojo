# Implementation Notes

**Candidate Name:** Coral Izquierdo Muñiz
**Date:** 29th November 2025
**Time Spent:** < 2 hours

---

## 📝 Summary

Brief overview of what you implemented and your overall approach.

---

## ✅ Completed

List what you successfully implemented:

- [x] `ingest_data()` - basic functionality
- [x] `ingest_data()` - deduplication
- [x] `ingest_data()` - sorting
- [x] `ingest_data()` - validation
- [x] `detect_anomalies()` - zscore method
- [ ] `detect_anomalies()` - additional methods (iqr/rolling)
- [ ] `summarize_metrics()` - basic statistics
- [ ] `summarize_metrics()` - quality metrics
- [ ] `summarize_metrics()` - time windowing
- [ ] Additional tests beyond exposed tests

---

## 🤔 Assumptions & Design Decisions

Document key assumptions and why you made certain design choices.

### Data Ingestion
- **Assumption 1:** I assumed that when validate argument is set to False, returns the dataframe without any sorting, deduplication, or type conversion
  - **Rationale:** the docstring specifies "If True, perform data validation". I interpreted this to mean that `False` should preserve the original state of the data, including potential errors and out-of-order timestamps.
  - **Alternative considered:** minimal structural cleanup like sorting by timestamp even when validation is skipped. I rejected this to ensure that when validate is set to False, it provides a true raw"view of the data.

- **Assumption 2:** I assumed `errors='coerce'` for the value validation.
  - **Rationale:** I imagine errors while sensor reading as "unknown" value.

- **Assumption 3:** I assume timestamp and sensor pairs.
  - **Rationale:** I imagine that a single sensor cannot produce two distinct readings at the exact same millisecond.

- **Assumption 4:** I filtered the quality when is set to "BAD"
  - **Rationale:** Because "BAD" data is explicitly flagged by the hardware as unreliable.

### Anomaly Detection
- **Method choice:** I implemented this code in z-score to prevent mathematical errors
    ```python
    if len(values) < 2 or pd.isna(std) or std == 0:
      raise ValueError("Insufficient data for zscore method")
    ```
- **Threshold handling:** I flagged data where the z_scores is greater than the threshold, and I used the absolute value to ensure that both positive and negative anomalies are considered.
- **Missing data:** NaN values are dropped strictly for the calculation of Mean and Std Dev to prevent error propagation.

### Metrics Summarization
- **Metric selection:** [Which metrics you chose and why]
- **Aggregation strategy:** [How you aggregate data]

---

## ⚠️ Known Limitations

Be honest about what doesn't work perfectly or edge cases you didn't handle.

### Edge Cases Not Fully Handled
1. **[Edge case 1]:** [e.g., "If all values for a sensor are NaN, my implementation..."]
   - **Impact:** [What breaks or degrades]
   - **Workaround:** [Temporary solution if any]

2. **[Edge case 2]:**
   - **Impact:**
   - **Workaround:**

### Performance Considerations
- **Large datasets:** [How your code scales, any concerns]
- **Memory usage:** [Any memory-intensive operations]

---

## 🚀 Next Steps

If you had more time, what would you improve or add?

### Priority 1: [Highest priority improvement]
- **What:** [Description]
- **Why:** [Impact/value]
- **Estimated effort:** [Time estimate]

### Priority 2: Implement "rolling" method
- **What:** Add rolling statistics to `detect_anomalies`.
- **Why:** To detect anomalies in time-series data where the mean changes over time.
- **Estimated effort:** 15 min.

### Priority 3: Implement "iqr" method
- **What:** Add iqr statistics to `detect_anomalies`.
- **Why:** Because IQR is more robust than Z-score as it relies on medians rather than means, making it less sensitive to extreme outliers.
- **Estimated effort:** 15 min.

### Additional Features
- [Feature idea 1]
- [Feature idea 2]

### Testing & Validation
- [What additional tests you'd write]
- [What validation you'd add]

---

## ❓ Questions for the Team

List any clarifying questions or areas where you'd like feedback.

1. **[Question about requirements]:** [e.g., "In production, how should we handle persistent connection failures?"]

2. **[Question about design]:** [e.g., "Would you prefer aggressive duplicate removal or conservative approach?"]

3. **[Technical question]:** [e.g., "Are there specific anomaly detection methods you use in production?"]

---

## 💡 Interesting Challenges

What did you find most interesting or challenging about this exercise?

- **Most challenging:** [What was hardest and why]
- **Most interesting:** [What you enjoyed working on]
- **Learned:** [Anything new you learned or researched]

---

## 🔧 Development Environment

Document your setup for reproducibility.

- **Python version:** [e.g., 3.11.5]
- **OS:** [e.g., Windows 11, Ubuntu 22.04, macOS]
- **Editor/IDE:** [e.g., VS Code, PyCharm]
- **Additional tools:** [e.g., "Used black for formatting", "Ran mypy for type checking"]

---

## 📚 References

Any resources you consulted (documentation, articles, etc.).

- [Resource 1 with link]
- [Resource 2 with link]

---

## 💭 Final Thoughts

Any additional context you want reviewers to know.

[Your thoughts here]

---

**Thank you for the opportunity!** I look forward to discussing this implementation.
