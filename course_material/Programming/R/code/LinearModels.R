
linearmodels <- function(filename)
{
  print(filename)
  layout(matrix(1:3,3,1))
  coronavirus2019dataset <- read.table(filename, header=TRUE)
  coronavirus2019dataset$mat <- cbind(coronavirus2019dataset$Total,coronavirus2019dataset$Perdiem)
  coronavirus2019logit1 <- glm(mat ~ Total + Perdiem, family = binomial(link = "logit"), data = coronavirus2019dataset)
  print("GLM - Logistic regression:")
  print(summary(coronavirus2019logit1))
  print(coronavirus2019logit1)
  print("=================================")
  coronavirus2019logit2 <- glm.fit(coronavirus2019dataset$mat, coronavirus2019dataset$Perdiem, family=poisson(link = "log"))
  print("GLM - Poisson Fit:")
  print(summary(coronavirus2019logit2))
  print(coronavirus2019logit2)
  print("=================================")
  coronavirus2019logit3 <- glm.fit(coronavirus2019dataset$mat, coronavirus2019dataset$Perdiem, family=gaussian(link = "identity"))
  print("GLM - Gaussian Fit:")
  print(summary(coronavirus2019logit3))
  print(coronavirus2019logit3)
  print("=================================")
  coronavirus2019logit4 <- glm.fit(coronavirus2019dataset$mat, coronavirus2019dataset$Perdiem, family=Gamma(link = "inverse"))
  print("GLM - Gamma Fit:")
  print(summary(coronavirus2019logit4))
  print(coronavirus2019logit4)
  print("=================================")
  coronavirus2019logit5 <- glm.fit(coronavirus2019dataset$mat, coronavirus2019dataset$Perdiem, family=inverse.gaussian(link = "1/mu^2"))
  print("GLM - Inverse Gaussian Fit:")
  print(summary(coronavirus2019logit5))
  print(coronavirus2019logit5)
  print("=================================")
  coronavirus2019logit6 <- glm.fit(coronavirus2019dataset$mat, coronavirus2019dataset$Perdiem, family=quasi(link = "identity", variance = "constant"))
  print("GLM - Quasi Fit:")
  print(summary(coronavirus2019logit6))
  print(coronavirus2019logit6)
  print("=================================")
  coronavirus2019logit7 <- glm.fit(coronavirus2019dataset$mat, coronavirus2019dataset$Perdiem, family=quasipoisson(link = "log"))
  print("GLM - QuasiPoisson Fit:")
  print(summary(coronavirus2019logit7))
  print(coronavirus2019logit7)
  print("=================================")
  coronavirus2019logit8 <- lm(Total ~ Perdiem, data = coronavirus2019dataset)
  print("LM - Linear regression:")
  print(summary(coronavirus2019logit8))
  print(coronavirus2019logit8)
  print("=================================")
  c(coronavirus2019logit1,coronavirus2019logit2,coronavirus2019logit3,coronavirus2019logit4,coronavirus2019logit5,coronavirus2019logit6,coronavirus2019logit7,coronavirus2019logit8)
}
covid19logit <- linearmodels("./LinearModels.dat")
print("Generalized Linear Models:")
print(covid19logit)
