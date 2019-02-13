#cloning the dataset 
!git clone https://gitlab.com/tihorchaudhary/financial-data-prediction.git
df = pd.read_csv(os.path.join('financial-data-prediction','hpq.us.txt'),delimiter=',',usecols=['Date','Open','High','Low','Close'])
print('Loaded data from the gitlab repository')
