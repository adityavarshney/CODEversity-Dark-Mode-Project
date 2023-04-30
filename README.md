# Project 2 🎤🎶🎧

Welcome to CODEversity Project 2. This project will take about 2 weeks and it will be due Week 7!

### Recap of the project so far

[Project 0](https://replit.com/@adityavarshney1/CODEversity-Spotify-P0) started with a simple app built with Flask. When we ran our app, a page opened up containing a header with the text "Hello world". Our website was born.

[Project 1](https://replit.com/@adityavarshney1/CODEversity-Spotify-P1) created a webpage that showcased our favorite music. To do this, we built HTML files for each page, added images into our project, and updated styling rules in CSS.

## Goals for Project 2

For this section, we want to use flask to make live updates to our page. To do this, we'll use flask's **templating**.

### Templating using Jinja

Under the hood, we've already been using `render_template` to allow our server running python to show our HTML and CSS. However, our templates so far have just been references to the HTML file itself and do not include any information from the back-end.

The core issue is that the HTML is static and does not change. Think of it like the skeleton of our webpage - it is just the structure and cannot do anything without muscles and a brain to move it around.

To allow our HTML to switch between light mode and dark mode, we will need some way to update our HTML and CSS based on what time it is.

We will first need to identify the time in Python and then send this information (along with any other information) to our front-end.

### Using placeholders

To pass values into our webpage from the back-end, we use `render_template`. 

`render_template` takes in the reference to the HTML page ("playlists.html") as well as any placeholder variables to show on the page.

This section has a lot of new content, so please take a careful look at the examples to better understand how Jinja syntax, Python, and HTML/CSS work together!

Other resources in case anything below is confusing:
* [RealPython's Primer on Jinja Templating](https://realpython.com/primer-on-jinja-templating/#use-an-external-file-as-a-template)
* [Flask's docs on Templates](https://flask.palletsprojects.com/en/1.1.x/tutorial/templates/)

#### Placeholder Variables

Let's suppose that we add the following code to our HTML:

```html
<p> {{ artist_name }} </p>
<p> {{ number_of_albums }} </p>
<p> {{ favorite_song }} </p>
```

This creates Jinja placeholders.

These are passed in to our template from our python code as follows: 
```python
artist_name = "Miguel"
number_of_albums = 4
favorite_song = "Sky Walker"

render_template("playlists.html", artist_name = artist_name, number_of_albums = number_of_albums, favorite_song = favorite_song)
```
Note that above, we are setting up our Python variables and then passing in the name of each variable to `render_template` to match up with a placeholder that we include in our HTML.

#### If statements

```html
<div>
  {% if n > 100 %}
  yay
  {% else %}
  boo
  {% endif %}
</div>
```
#### For loops 

```html
<div>
  <ul>
    {% for item in my_list %}
    <li> {{ item }} </li>
    {% endfor %}
  </ul>
</div>
```

### Templating Example

Let's consider an example. Suppose we want to show the time that the user arrived on the page.

First we'll write some code that will get the time for us and print it nicely in a string. 

```python
# we'll use this library to get a timestamp
from datetime import datetime 

# code that formats a timestamp into dd/mm/yy hh:MM:SS format
def format_time(time_obj):
  return time_obj.strftime("%m/%d/%Y %H:%M:%S")

# code that gets the time using datetime.now()
def get_time(): 
  # returns a string with the time
  return datetime.now()
```

Then we'll call flask's `render_template` function and pass in the final formatted time to a placeholder variable called **current_time**.

```python
# renders time.html 
@app.route("/time")
def create_time_page():
  # get and format the time 
  current_time = get_time()
  formatted_time = format_time(current_time)

  # pass the formatted time to the HTML template
  return render_template(
    "time.html",
    current_time=formatted_time 
)
```

Then in our `time.html` file we will use **Jinja syntax** to add the **current_time** placeholder variable in our code. The name of our placeholder in the HTML has to be the same as the placeholder used in `render_template` for flask to assign the correct value.

```time.html
<body>
    <h1> Congrats! </h1>
    <p> You opened this page at: {{ current_time }} </p>
</body>

```

With this example in place, let's look at some more interesting uses of templating!
____

## Recommended Concerts!

In `recommendations.html`, we showcased our favorite songs, albums, and artists. 

This exercise takes it one level further &ndash; let's support our artists by providing our users links to their next shows. 

1. For any artists in your recommended list that are still performing, search online for their upcoming shows. If none of your artists are performing, add 

2. Build a python list of strings that contain information about the concerts you've discovered. 

For example:
```
"See 5 Seconds of Summer live at Concord Pavilion on Tuesday 14 June 2022"
```

🌶️ **SPICY** 🌶️: Create a python list of tuples. A tuple is a collection of items that cannot be modified after it's created. Each tuple will split up the string above into logical pieces, such as (artist, venue, date) for example. 

```
concerts = [
  ('5 Seconds of Summer', 'Concord Pavilion', 'Tuesday 14 June 2022')
]
```
This approach will allow us to add styling to the different elements in our recommended concert.

3. Create a python list in `main.py` that contains the concert information strings.

4. Pass the list as an argument to the `/recommendations` route's `render_template` function. **Remember, `render_template` will let you pass information from the back-end (main.py) to the front-end (recommendations.html).** Don't forget to use a template placeholder. 

For example:
```
render_template("recommendations.html", <placeholder>=<your list variable here>)
```

5. In `recommendations.html` add an unordered HTML list. This will be where we list out the upcoming concerts.

6. Inside that, add a for-loop template statement. See the [For Loops](#for-loops) section above if you need a refresher.

7. In the loop, iterate through each concert string (🌶️ tuple) in your placeholder list. For each string, create an HTML paragraph `<p></p>` and pass in the string as the paragraph text.

For example:
```
<ul class="my-unordered-list">
  <--! for loop jinja syntax here-->
    <p> value of the list element goes here <p>
  <--! end for loop -->
</ul>
```
For those spicy folks ~ 🌶️ ~ use a `<span><span>`, you likely have a list of tuples instead of a list of strings in your list. To show the user your recommended date, add some text in the paragraph that gives a full recommendation. Then use `<span>{your element item here}<span>` 

8. Upgrade your design by wrapping the paragraphs in `<div></div>` tags with `class=` attributes and adding CSS styling rules for those. Make the page pop!

🌶️🌶️🌶️ Also add custom styling for each of the span types (artist, venue, location) to spice up your page. Use `class=` attributes.
Things to try:
```
* Change the font or color of the span item, depending on if it corresponds to an artist, a venue, or a location
* Create CSS classes that modify the opacity for concerts happening this week, happening this month, and happening down the line. 
```

9. **MILD** Add even more information to the concert listing. Can you find ticket prices, links to buy tickets, merch images? From start to finish, what changes would you need to make to show these elements to the user. 

10. **MILD** Update the `<p>` tags to be `<div>` tags that lay out these different pieces of information in a nice format.

___

## Dark mode

Suppose we want to add a dark mode or light mode feature to our page. Something like this:

![image](image.png)

☀️ Between 6:00 AM and 6:00 PM, inclusive, the website is in light mode. ☀️

🌙 Between 6:00 PM and 6:00 AM, the website is in dark mode. 🌙

#### QUESTION: How do we get the time?
To get the time we'll use the datetime library from before. We'll compare this time with some other times:

```python
from datetime import datetime, time 

# get the current time object
# for example: datetime.time(4, 16, 1, 504774)
def get_current_time():
  return datetime.now().time()

# create a time object (24 hour clock)
# for example: get_time(1, 0, 0) -> datetime.time(1, 0)
def get_time(hours, minutes, seconds):
  return time(hours=hours, minutes=minutes, seconds=seconds)
```

#### QUESTION: How do we figure out if we need light mode or dark mode? 

```python
# compare the current time with 6:00 PM and 6:00 AM
# return True if we need to be using light mode
# return False if we should use dark mode
# Hint: compare get_current_time() with the result from get_time(...) at *specific* times in the day to find out if we should choose light mode or dark mode.
def use_light_mode():
  print("YOUR CODE HERE")
```


#### QUESTION: How do we pass our light/dark mode decision to our front-end?

Pass the result of `use_light_mode` into `render_template` with a placeholder (maybe call it `light_mode`).


#### QUESTION: How do we update our web theme to be dark mode? 

Two options:
1. Add an if-statement template around the `<link>` tag that connects the webpage with another style-sheet. This approach is best for intricate modes.
2. Add an if-statement template around a `<style>` tag that contains custom CSS to handle one of the modes. This approach is good if your light mode only involves a few changes.

#### QUESTION: How do we update our styles based on the time?

- We could update which stylesheet we use. If we are using light mode, pick a stylesheet with lighter colors. If not, use a stylesheet with darker colors.

In the html files:
```html
{% if ... %} 
  <link rel="stylesheet" href="...">
{% else %} 
  <link rel="stylesheet" href="...">
{% endif %}
```

- We can use templating with `<style>` tags. If it's the time for light mode, we don't do anything (light mode is default). If it's time for dark mode, we use a different set of styles

In the html files:
```html
{% if ... %}  <--! check if it's time for dark mode -->
  <style>
    // add dark mode css
  </style>
{% endif %}
```

#### Add light/dark mode to all pages in your webpage

Now that you've got light/dark mode working, make sure all pages in your site implement it!
