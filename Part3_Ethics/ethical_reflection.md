# Part 3: Ethical Reflection

## Scenario
Your predictive model from Task 3 is deployed in a company to automatically prioritize software issues and allocate development resources accordingly.

---

## 1. Potential Biases in the Dataset

### A. Historical Bias
**Issue**: The training data reflects past human decisions about issue prioritization. If previous teams consistently underestimated certain types of issues (e.g., accessibility bugs, security vulnerabilities in less-used features), the model will learn and perpetuate this bias.

**Example**: If historically, issues reported by junior developers were marked as "low priority" more often than those from senior developers, the model might learn to deprioritize issues based on reporter seniority rather than actual impact.

### B. Representation Bias (Underrepresented Teams)
**Issue**: If the dataset predominantly contains issues from certain teams, products, or user demographics, the model will perform poorly for underrepresented groups.

**Example**: 
- A dataset with 90% issues from the web team and only 10% from the mobile team will result in a model that's less accurate for mobile issues
- If most training data comes from English-speaking markets, issues affecting international users might be misclassified
- Issues affecting users with disabilities might be underrepresented if accessibility testing was historically deprioritized

### C. Temporal Bias
**Issue**: Software priorities change over time. A model trained on data from 2020 might not understand that security and privacy issues are now higher priority than they were then.

**Example**: Pre-GDPR data would underestimate the priority of data privacy issues compared to post-GDPR requirements.

### D. Measurement Bias
**Issue**: The features used to train the model might not capture the full context of an issue's importance.

**Example**: 
- An issue affecting 100 enterprise customers might be labeled "low priority" based on raw user count, while an issue affecting 10,000 free-tier users is "high priority"
- The model doesn't understand that the 100 enterprise customers represent 80% of revenue

### E. Label Bias
**Issue**: The "ground truth" labels themselves might be biased based on who assigned them.

**Example**: If only senior engineers labeled training data, their perspective might not reflect the priorities of customer support, sales, or end users.

---

## 2. How Fairness Tools Like IBM AI Fairness 360 Could Address These Biases

### A. Bias Detection Metrics

**IBM AIF360 Implementation**:
```python
from aif360.datasets import BinaryLabelDataset
from aif360.metrics import BinaryLabelDatasetMetric

# Define protected attributes (e.g., team, reporter role, user segment)
protected_attributes = ['team_id', 'reporter_seniority']

# Create dataset with protected attributes
dataset = BinaryLabelDataset(
    df=training_data,
    label_names=['priority'],
    protected_attribute_names=protected_attributes
)

# Calculate fairness metrics
metric = BinaryLabelDatasetMetric(dataset, 
                                  unprivileged_groups=[{'team_id': 'mobile'}],
                                  privileged_groups=[{'team_id': 'web'}])

print(f"Disparate Impact: {metric.disparate_impact()}")
print(f"Statistical Parity Difference: {metric.statistical_parity_difference()}")
```

**Impact**: This reveals if certain teams' issues are systematically deprioritized, quantifying the bias before deployment.

### B. Bias Mitigation Algorithms

**1. Pre-processing: Reweighing**
```python
from aif360.algorithms.preprocessing import Reweighing

# Reweigh training samples to ensure fair representation
RW = Reweighing(unprivileged_groups=[{'team_id': 'mobile'}],
                privileged_groups=[{'team_id': 'web'}])
dataset_transformed = RW.fit_transform(dataset)
```

**How it helps**: Assigns higher weights to underrepresented groups' data points, ensuring the model learns equally from all teams.

**2. In-processing: Prejudice Remover**
```python
from aif360.algorithms.inprocessing import PrejudiceRemover

# Train model with fairness constraint
PR = PrejudiceRemover(sensitive_attr='team_id', eta=1.0)
PR.fit(dataset)
```

**How it helps**: Modifies the learning algorithm itself to reduce discrimination during training.

**3. Post-processing: Equalized Odds**
```python
from aif360.algorithms.postprocessing import EqOddsPostprocessing

# Adjust predictions to achieve equal true positive rates across groups
EO = EqOddsPostprocessing(unprivileged_groups=[{'team_id': 'mobile'}],
                          privileged_groups=[{'team_id': 'web'}])
dataset_pred_transformed = EO.fit_predict(dataset_valid, dataset_pred)
```

**How it helps**: Adjusts the model's predictions to ensure equal accuracy across all teams without retraining.

### C. Fairness-Aware Model Evaluation

**Continuous Monitoring**:
```python
# Monitor fairness metrics in production
from aif360.metrics import ClassificationMetric

cm = ClassificationMetric(dataset_true, dataset_pred,
                         unprivileged_groups=[{'team_id': 'mobile'}],
                         privileged_groups=[{'team_id': 'web'}])

print(f"Equal Opportunity Difference: {cm.equal_opportunity_difference()}")
print(f"Average Odds Difference: {cm.average_odds_difference()}")
```

**Impact**: Enables ongoing detection of bias drift as new data arrives.

### D. Explainability Integration

**Combining AIF360 with SHAP/LIME**:
```python
import shap

# Explain individual predictions
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)

# Identify if protected attributes are influencing decisions
shap.summary_plot(shap_values, X_test)
```

**How it helps**: Reveals if the model is making decisions based on protected attributes (team, reporter role) rather than issue merit.

---

## 3. Recommended Mitigation Strategy

### Step 1: Audit the Dataset
- Use AIF360 to measure existing biases across teams, products, and user segments
- Document disparate impact scores

### Step 2: Apply Pre-processing
- Reweigh underrepresented groups
- Ensure balanced representation in training data

### Step 3: Train with Fairness Constraints
- Use prejudice remover or adversarial debiasing during model training
- Set fairness thresholds (e.g., disparate impact > 0.8)

### Step 4: Post-process Predictions
- Apply equalized odds to ensure equal accuracy across groups
- Validate that no group has significantly worse false negative rates

### Step 5: Monitor in Production
- Implement real-time fairness dashboards
- Set alerts for fairness metric degradation
- Regularly retrain with updated, more representative data

### Step 6: Human-in-the-Loop
- For borderline cases, require human review
- Allow teams to flag misprioritized issues for model retraining

---

## Conclusion

Deploying AI for resource allocation without bias mitigation risks:
- **Operational inefficiency**: Important issues from underrepresented teams get ignored
- **Team morale**: Teams feel their work is systematically undervalued
- **Customer impact**: Issues affecting minority user segments are deprioritized
- **Legal risk**: Discrimination in resource allocation could violate employment laws

**IBM AI Fairness 360 provides a comprehensive toolkit** to detect, measure, and mitigate these biases, ensuring the AI system serves all teams and users equitably. The key is to treat fairness as a continuous process, not a one-time check.
