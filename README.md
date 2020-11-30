<body>
<h1>RECIPE ROULETTE</h1>
<p>A recipe application to help people decide what to cook for dinner, including the choice for random recipe suggestions (recipe roulette).</p>

<h1>The App</h1>
<p>I made an app to help resolve users' indecision around what to cook. They can choose from a recipes list, get a recipe at random, or create and manipulate a favourites list as they so wish. This application was built following the product backlog and user requirements (See the link to the Trello below, under Technologies/Tools Used). Risk Assessment issues were also considered (see picture below). </p>
<img src="https://imgur.com/BiZkoYH.png">

<h1>Entity Relationship Diagrams</h1>
<img src="https://i.imgur.com/sA6jOZ1.png">
<p>Users can have an account and have a favourite recipes list. Originally there were just two tables , the Users and Recipes. I added the favourites table as I wanted Users to be able to make favourites and then access their favourite recipes quickly without going through the whole list of recipes on the app. They can also delete from their favourite recipes list if they wish.
</p>

<h1>Deployment</h1>
<p>The Jenkins CI Server was used to automate the test and build process. I made sure the app was working before trying the deployment to save time in potential errors.</p>

<h1>Technologies/Tools Used</h1>
<p><a href="https://trello.com/b/4iumgJyC/personal-sfia-project-tracking">Trello</a></p>
<p>Google Cloud Platform</p>
<p>MySQL</p>
<p>Python</p>
<p>Jenkins - CI Server</p>
<p>Git - VCS</p>

<h1>Integrating Changes</h1>
<p>I integrated change requests as neccesary. It started off as a simple recipe app. However, the need arose for the users to have their favourite recipes in one place, and also be able to modify their account details themselves. Therefore, I built a Favourites feature into the app, and added functionality that enables the user to update their account details themselves. I made time for these extra features to be added, tested and built, so that the application could be delivered on time and to specification. The addition of microservices will also help me to perform maintenance as necessary while minimising downtime as much as possible.</p> 

<h1>Future Improvements</h1>
<p>In coming updates, I would like to make sure all user account info is deleted along with the user account. This ensures that minimal space is taken up on the database.</p>
<p>I would also like to promote better user security - requiring the user to make their password more secure by requiring use of upper case and lower case characters, and number/special characters when creating their password. </p>
<p>I also plan to add a an extra step that double checks if the user is sure that they want to delete their account when they click delete.</p>

<h1>Alexandra Akrong</h1>

</body>
</html>
