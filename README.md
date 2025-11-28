# AI in Software Engineering Assignment

**Theme**: "Building Intelligent Software Solutions" 💻🤖

This repository contains the complete implementation of the AI in Software Engineering assignment, demonstrating how AI automates tasks, enhances decision-making, and addresses challenges in software development.

---

## 📁 Project Structure

```
AI_Software_Engineering_Assignment/
│
├── Part1_Theory/
│   └── theory_report.md                    # Theoretical analysis and case study
│
├── Part2_Practical/
│   ├── Task1_Code_Completion/
│   │   ├── task1_code_completion.py        # Manual vs AI code comparison
│   │   └── task1_analysis.md               # 200-word comparative analysis
│   │
│   ├── Task2_Automated_Testing/
│   │   ├── task2_login_test.py             # Selenium automated test suite
│   │   └── task2_summary.md                # AI testing improvements summary
│   │
│   └── Task3_Predictive_Analytics/
│       └── task3_predictive_analytics.ipynb # Jupyter notebook with ML model
│
├── Part3_Ethics/
│   └── ethical_reflection.md               # Bias analysis and mitigation
│
├── Bonus/
│   └── ai_tool_proposal.md                 # CodeDoc AI proposal
│
├── Presentation/
│   └── presentation_content.md             # 3-minute video script
│
└── README.md                                # This file
```

---

## 🎯 Assignment Overview

### Part 1: Theoretical Analysis (30%)
- **Q1**: How AI code generation tools reduce development time and their limitations
- **Q2**: Supervised vs unsupervised learning for bug detection
- **Q3**: Importance of bias mitigation in UX personalization
- **Case Study**: AIOps improving deployment efficiency

### Part 2: Practical Implementation (60%)

#### Task 1: AI-Powered Code Completion
- Implemented dictionary sorting function manually and with AI suggestions
- Performance comparison showing 15-20% improvement with `operator.itemgetter`
- **Key Learning**: AI tools suggest optimized patterns from standard libraries

#### Task 2: Automated Testing with Selenium
- Built comprehensive login page test suite
- Tests: valid login, invalid username, invalid password, empty credentials
- **Key Learning**: AI-enhanced testing provides self-healing and intelligent test generation

#### Task 3: Predictive Analytics for Resource Allocation
- Trained Random Forest model for issue priority prediction
- **Metrics Achieved**:
  - Accuracy: 96%
  - F1-Score: 0.97
  - Cross-validation F1: 0.96 (±0.02)
- **Application**: Automated issue triage and developer allocation

### Part 3: Ethical Reflection (10%)
- Identified 5 bias types: historical, representation, temporal, measurement, label
- Proposed mitigation using IBM AI Fairness 360
- Emphasized continuous monitoring and human-in-the-loop validation

### Bonus: Innovation Challenge (10%)
- **Proposed Tool**: CodeDoc AI
- **Purpose**: Automated documentation generation and maintenance
- **Impact**: 80% reduction in documentation time, 50% faster onboarding

---

## 🚀 How to Run

### Prerequisites
```bash
# Install required packages
pip install numpy pandas matplotlib seaborn scikit-learn selenium jupyter

# For Selenium tests, install ChromeDriver
# Download from: https://chromedriver.chromium.org/
```

### Task 1: Code Completion
```bash
cd Part2_Practical/Task1_Code_Completion
python task1_code_completion.py
```

### Task 2: Automated Testing
```bash
cd Part2_Practical/Task2_Automated_Testing
python task2_login_test.py
```

### Task 3: Predictive Analytics
```bash
cd Part2_Practical/Task3_Predictive_Analytics
jupyter notebook task3_predictive_analytics.ipynb
```

---

## 📊 Key Results

| Task | Metric | Result |
|------|--------|--------|
| Code Completion | Performance Improvement | 15-20% faster |
| Automated Testing | Test Coverage | 4 scenarios automated |
| Predictive Analytics | Accuracy | 96% |
| Predictive Analytics | F1-Score | 0.97 |

---

## 🎥 Presentation

A 3-minute video demonstration is available covering:
1. AI-powered code completion comparison
2. Automated testing demo
3. Predictive analytics model performance
4. Ethical considerations
5. CodeDoc AI innovation

**Script and slides**: See `Presentation/presentation_content.md`

---

## 📚 Technologies Used

- **Languages**: Python 3.8+
- **ML Libraries**: Scikit-learn, NumPy, Pandas
- **Testing**: Selenium WebDriver
- **Visualization**: Matplotlib, Seaborn
- **Development**: Jupyter Notebook

---

## 🤝 Contributors

[Your Team Members' Names Here]

---

## 📄 License

This project is submitted as part of the AI in Software Engineering course assignment.

---

## 🔗 Resources

- [GitHub Copilot Documentation](https://github.com/features/copilot)
- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [Scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [IBM AI Fairness 360](https://aif360.mybluemix.net/)

---

**Submission Date**: [Add Date]  
**Course**: AI in Software Engineering  
**Assignment**: Week 4 - Building Intelligent Software Solutions
