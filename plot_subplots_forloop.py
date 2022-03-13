cols, rows = 3, 2

fig, axes = plt.subplots(rows, cols, figsize=(16,12))

columns = ['CreditLimit', 'CreditUsed', 'AmountRepaid', 'Balance', 'Fees', 'DaysOverdue']


for index, col in enumerate(columns):
    # new subplot with (i + 1)-th index laying on a grid
    plt.subplot(rows, cols, index + 1) 
    # drawing the plot
    sns.boxplot(x='cleared_cat', y=col, data=data)
    plt.title(f"{col}")

fig.suptitle("Numerical columns in relation to Cleared status")
plt.show()
