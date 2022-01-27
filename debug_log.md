# Debug Log

**Explain how you used the the techniques covered (Trace Forward, Trace Backward, Divide & Conquer) to uncover the bugs in each exercise. Be specific!**

In your explanations, you may want to answer:

- What is the expected vs. actual output?
- If there is a stack trace, what useful information does it contain?
- Which technique did you use, on which line numbers?
- What assumptions did you have about each line of code, and which ones were proven to be wrong?

_Example: I noticed that the program should show pizza orders once a new order is made, and that it wasn't showing any. So, I used the trace forward technique starting on line 13. I discovered the bug on line 27 was caused by a typo of 'pzza' instead of 'pizza'._

_Then I noticed another bug ..._

## Exercise 1

The expected output was to show pizza orders on the home page and be able to submit them and order them via a form, and the actual output was the orders not showing.
My initial assumptions were that the parameters were not correctly being passed into the pizza class, and that the Jinja variables were not being accessed correctly. The Jinja assumption was proven to be wrong.
I used the trace backward techniquestack trace and error messages to realize I needed a for loop to iterate through topping_list, and change the attribute and change redirect to home
pizza_size and order_name. Also added backref = 'pizza' to the database, and db.session.commit() was missing, it must be added after the order parameters were passed. Lastly, the redirect must be to url_for home rather than /.

## Exercise 2

The expected output is to show the information of the city and parameters I enter, the actual output was an error message.
My first assumptions were that there was a misspelling, or that the API was not being accessed properly. These were proven to be correct, though they were general.
I used the trace forward technique and realized that instead of retrieving the city name from the API, you mustretrieve it from the user and in the params, you must get latitiude and longitude using a function. I also discovered that the date was not being properly accessed.

## Exercise 3

The expected output is to print two sorted arrays, the actual output is getting error messages in the terminal.
My assumptions were that there was an error in one of the loops for merge sort and for binary search, floor division was not occuring and there was a typo. Both of these assumptions were correct, but there turned out to be more errors.
I used the divide and conquer technique and analyzed two different parts of code, using log statements to deduce the problem. I realized that while traversing the left and right sides, the if statement should be less than: if left_side[i] < right_side[j]. Also, right_side[i] should be right_side[j] since it is accessing the jth index, and k must be incremented by 1 each time it adds the remaining elements of the left and right arrays. For binary search, floor division should occur when finding the midpoint. If the element is less than current, then the low should be set equal to the midpoint minus one, and vice versa.