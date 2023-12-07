rule prepare:
    output: "./data/wine.data"
    script: "./scripts/prepare_data.py"

rule profile:
    input: "./data/wine.data"
    output: "./profiling/report.html"
    script: "./scripts/profile.py"

rule analyze:
    input: "./data/wine.data"
    output: 
        "./results/linear_regression_plot.png",
        "./results/mean_sqaured_error.txt",
        "./results/summary_statistics.csv"
    script: "./scripts/analyze.py"

