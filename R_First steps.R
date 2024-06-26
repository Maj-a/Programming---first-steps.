####### First Steps in R - Programming Basics in R 

##  0. Instaling packages and libraries
library("stringr")

## 1. Create a matrix with three rows A, B and C 
#     and four columns with names Q, W, E and R. 
#     Fill the matrix with any numbers between 1 and 10.

MS_matrix<-matrix(1:10, byrow=TRUE, nrow=3, ncol=4)
MS_matrix
rownames(MS_matrix)<-c("A", "B", "C")
colnames(MS_matrix)<-c("Q", "W", "E","R")
MS_matrix

## 2. x = 24, y =”Hello World”, z = 93.65.
#     Identify the class of x, y and z and convert all three into factor.

# Assigning values - Needed to change = to <- 
x <- 24
y <- "Hello World"
z <- 93.65

# checking the types of variables
class(x)
class(y)
class(z)

# converting to factor
x <- factor(24) 
y <- factor("Hello World")
z <- factor(93.65)

# checking the variables types:
class(x)
class(y)
class(z)

## 3. q = 65.9836
#     a. Find square root of q and round it up to 3 digits.
#     b. Check if log to the base 10 of q is less than 2.

q<-65.9836

# a)
q_sqrooted<-sqrt(q)
q_sqrooted
q_rounded<-round(q_sqrooted, digits = 3)
q_rounded

# b) 
q_log10<-log10(q)
q_log10

q_log2<- log2(q)
q_log2

Question_1<- q_log10 < 2
print(paste("Is q_log10 smaller then 2. The answer is: ", Question_1)) 
Question_2<-q_log10 < q_log2
print(paste("Is q_log10 smaller then log2. The answer is: ", Question_2))

## 4. x = c(“Intelligence”, “Knowledge”, “Wisdom”, “Comprehension”) 
#     y = “I am”
#     z = “intelligent”
#     a. Find first 4 letters of each word in x.
#     b. Combine y and z to form a sentence “I am intelligent”
#     c. Convert all the words in x to upper case.

#changing = to <- and change curly double quotation to straight double quotation

x <- c("Intelligence", "Knowledge", "Wisdom", "Comprehension")
y <- "I am"
z <- "intelligent"

# Answer a)

str_sub(x, start=0, end=4)

# Answer b)
print(paste(y, z))
cat(y,z)

# Answer c)

Answer_4c<-str_to_upper(x)
cat("Words in vector x converted to upper case:", Answer_4c, "\n")
toupper(x)

## 5. a = c(3,4,14,17,3,98,66,85,44)
#     Print “Yes” if the numbers in ‘a’ are divisible by 3  
#      and “No” if they are not divisible by 3 using ifelse().

a <- c(3,4,14,17,3,98,66,85,44)
ifelse(a%%3==0,"Yes","No")

## 6. b = c(36,3,5,19,2,16,18,41,35,28,30,31)
#     List all the numbers less than 30 in b using for loop.

b <- c(36,3,5,19,2,16,18,41,35,28,30,31)
for(num in b){
  if(num<30){
    print(num)
  }
}

## 7. Date = “01/30/18”
#     a) Convert Date into standard date format (yyyy-mm-dd) and name it as Date_new.
#     b) Extract day of week and month from Date_new.
#     c) Find the difference in the current system date and Date_new.

# updating assign sign <- from =, also changing to "" 

# a)
Date<-"01/30/18"
Date_asDate<-as.Date(Date, format="%m/%d/%y")
Date_asDate
Date_new1<- format(Date_asDate, "%Y-%m-%d")
Date_new<-as.Date(Date_new1)

Date_new
class(Date_new)

# b)

day_of_week <- weekdays(Date_new)
day_of_week
month <- months(Date_new)
month

# c)

today<-Sys.Date()
today
Difference=today-Date_new
Difference
