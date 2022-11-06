getwd()
setwd('path')
list.files()

read.table("norm.nao.monthly.b5001.current.ascii04Nov2022.txt", header = FALSE, sep = "", dec = ".")
dim(df)
names(df) # columns of df
df$V1 # get column V1
df["V3"]
arima(df["V3"], order=c(0, 0, 1))
