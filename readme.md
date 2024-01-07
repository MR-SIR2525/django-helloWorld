# Andrew's Page of Django

This hello world project is a project I began in early fall 2022 and kept building on top of for each assignment in my Full-Stack Web Dev class. It is the accumulation of a lot of work spread out over the semester. It was built using Python 3.9.6, 3.10, and now 3.11, and Django 4.0.4.

For the latest assignment, for the CRUD functionality, the way I wanted my forms to work resulted in me basically re-inventing multiple wheels. However, I feel that I have a better understanding of how forms work, and how to use Crispy forms. And, my forms don't look half bad.

I used the background image code, the basic html skeleton, and the CSS from sources below. I have altered and added a lot of my own CSS. The random background pictures are from unsplash.com

-----
I think I should make this a sort of portfolio site in the future...


## Works Cited, References
* [W3Schools Templates- Startup](https://www.w3schools.com/w3css/tryw3css_templates_startup.htm)
* [Random background img from unsplash.com](https://source.unsplash.com/random/1366x768)
* [Fetch Data From a Database And Output To A Webpage](https://www.youtube.com/watch?v=H3joYTIRqKk)
* [Template Tag: getattribute code and usage](https://stackoverflow.com/a/1112236)
* [Model update view](https://www.geeksforgeeks.org/update-view-function-based-views-django/)


### For car stats, I used:
* Official Manufacturer/car brand websites 
* caranddriver.com
* motortrend.com

### For my own future reference:
* [base.html info](https://stackoverflow.com/questions/14720464/django-project-base-template)
* [How to use crispy forms](https://simpleisbetterthancomplex.com/tutorial/2018/11/28/advanced-form-rendering-with-django-crispy-forms.html#crispy-forms-layout-helpers)



## Change Log 
January 2024:
  1. Integrate Docker stuff to 'docker-integration' branch; update readme

August 2023: 
  1. Fix 'all three' carstats page - needs to display all the tables
  2. Consolidate car-related tables
  3. Automobile forms:  make some of the fields not required.

2022:
* Module 5.1: update form added. Delete form redone to be like update form. Looks good.

* Module 5: forms added to create and delete Automobiles. Crispy forms installed. Update not implemented yet.

* Module 4: added a page for Automobile, ICE Car, and Electric Car models. Changed views to classes that inherit from django's generic ListView. I also made those pages all use the same template/html file and made Django dynamically populate the relevent material (interesting, took me a lot of time to figure out).

* Module 3: altered readme file and improved some formatting

* Module 2: added navigation, added new page for tables of car stats for database assignment that uses for loop and django template utility

* Module 1: removed some body content sections, navigation, and added random background ability. I was using picsum to get random pictures but their service for delivering the image via a link
was a lot slower than unsplash's. However, picsum has a much better selection of random pictures.