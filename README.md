# Project-Fisher-Iris-Data-Set
My project for the Programming and Scripting module.

The, slightly erroneously named, Fisher Iris Data Set was created by Edgar Anderson, though Sir Ronald Aylmer Fisher is often credited 
with this due to his highly influential analysis of the data set itself. Fisher was a British statistician and geneticist, and is 
considered one of the most important people in 20th century statistical analysis. He used linear discriminant anlysis to distinguish 
between the different iris species.

He used this particular method as he considered it the best linear function to maximise the difference in ratio between
the different species of plants. This effectively just made it easier to distinguish between the different species based on the different
means and standard deviations of the the data available, specifically, the sepal and petal lengths and widths.

This data set is still in use today, perhaps most notably in teaching materials related to machine learning (learning some properties of a
data set and testing those properties against another data set), which typically uses some sort of algorithm to help classify the data. In
layman's terms, the data is input, and the machine learning algorithm will output the class that that data is most likely to belong to.

This particular data set has been analysed extensively over the years so I doubt this presentation of the data will add anything new. That 
being said, in this project I decided to compare the different sepal and petal lengths and widths within their own species. Typically for
this data set these are compared accross species, similar to what Fisher originally did himself, but there appears to be less in terms of
analysis within their own species. 

This was done just to try add a somewhat different take on the norm. How do the different measurements vary within their own species, 
is there any relationship, for example, between the sepal length and width of any of them, or does that just appear to be the case with one 
particular species but not the others. This allows us to not only get a better grasp of the within species differences with regards to 
these different variables, but as we have that data compared as such, we can still examine the differences between species too. For example, 
comparing the distribution of the sepal lengths of the Iris Setosa against the Iris Virginia etc...

Also, apologies for the day late submission of this project. I had my code working, mostly, tried to do some fancy improvements in seaborn
and use nested loops and other things and ended up completely butchering the original code, meaning a lot of it had to be done again. 
Thankfully I managed to keep some of the seaborn improvements so the graphs should look quite nice.
