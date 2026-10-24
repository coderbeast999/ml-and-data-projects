# ML and Data Projects

Projects I built during the Girls Who Code Data Science and Machine Learning courses (July to August 2026). I used Python, pandas, matplotlib and scikit-learn.

Note: these programs import `GWCutilities`, a helper file provided by Girls Who Code. The analysis, model choices and interpretation are mine. The datasets were provided through the program and are included in each folder so the code can run.

## 1. Heart disease prediction (decision tree)

I trained a decision tree classifier to predict whether a person has heart disease, using health-survey data.

- Test accuracy: 74.4%. Train accuracy: 78.2%.
- Only 8% of the test patients had heart disease, so a model that always said "no" would score about 92%. That means accuracy alone isn't a good measure here. I balanced the classes and looked at recall: the model caught 67% of the real cases, but its precision was only about 20%, so it raised a lot of false alarms.
- Next I would like to try limiting the depth of the tree and comparing it with other models.

## 2. Age of marriage vs. education in India

I plotted women's average years of schooling and their average age at marriage in India over time.

- Both rose steadily. Because both go up over time, this alone doesn't prove that one causes the other.
- My research question: what factors besides education help raise the age at marriage?

