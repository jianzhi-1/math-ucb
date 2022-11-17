getwd()
setwd('path')
list.files()

read.table("norm.nao.monthly.b5001.current.ascii04Nov2022.txt", header = FALSE, sep = "", dec = ".")
dim(df)
names(df) # columns of df
df$V1 # get column V1
df["V3"]
arima(df["V3"], order=c(0, 0, 1))

# difference array
arima(diff(diff(df$MRTSSM4453USN, lag=12)), order=c(0,0,1))

# prediction and plotting
pred = predict(arima(df$MRTSSM4453USN, order=c(0,0,2)), n.ahead=36)
plot(1:(length(df$MRTSSM4453USN) + length(pred$pred)), c(df$MRTSSM4453USN, pred$pred), type="l")
