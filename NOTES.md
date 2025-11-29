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

- [ ] `ingest_data()` - basic functionality
- [ ] `ingest_data()` - deduplication
- [ ] `ingest_data()` - sorting
- [ ] `ingest_data()` - validation
- [ ] `detect_anomalies()` - zscore method
- [ ] `detect_anomalies()` - additional methods (iqr/rolling)
- [ ] `summarize_metrics()` - basic statistics
- [ ] `summarize_metrics()` - quality metrics
- [ ] `summarize_metrics()` - time windowing
- [ ] Additional tests beyond exposed tests

---

## 🤔 Assumptions & Design Decisions

Document key assumptions and why you made certain design choices.

### Data Ingestion
- **Assumption 1:** [e.g., "Assumed that duplicates should be identified by identical timestamp + sensor + value"]
  - **Rationale:** [Why you made this choice]
  - **Alternative considered:** [What else you thought about]

- **Assumption 2:** [e.g., "Chose to keep 'BAD' quality readings but flag them"]
  - **Rationale:** [Why]

### Anomaly Detection
- **Method choice:** [Why you implemented certain methods]
- **Threshold handling:** [How you handle edge cases with thresholds]
- **Missing data:** [How you handle NaN values in anomaly detection]

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

### Priority 2: [Second priority]
- **What:**
- **Why:**
- **Estimated effort:**

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
