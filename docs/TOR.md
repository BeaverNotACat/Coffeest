# General
## Target
Create an application for managing and sharing coffee-brewing recipes
## Audience
Coffee enthusiasts in need of storing and researching share their own and others’ recipes
## Landing page
**When visible:** Default view for unregistered or logged-out visitors
- **Search bar** for finding recipes by coffee type, brewing tool, or author name
- **Login** button
- **Recipe list:** Cards showing all recipes, paginated and sorted chronologically
## User profile
**When visible:** Default view after logging in.
- **Search bar** (same functionality as on Main page)
- **Profile icon** with rating
- **My Recipes:** Cards showing only the user’s own recipes, paginated and sorted chronologically
- **Add Recipe** button
- **My Tools:** Cards for each brewing device the user owns, each with a “Remove” button in corner
- **Add Tool** button
## Recipes search
**When visible:** After submitting a query from any search bar
- **Search bar** with text input (retains your query)
- **Recipe list:** Cards of matching recipes, paginated
## Recipe detail view
**When visible:** After clicking any recipe card
- **Tools Used:** List of brewing tools
- **Parameters:** Grind size, coffee weight, water temperature, total brew time, totals time and total water required
- **Pour Steps:** Detailed list of water additions (weight + time)
- **Score Sheet:** Either display an existing score sheet or show an “Add Score Sheet” button
## Add Tool
**When visible:** After clicking “Add Tool”
- **Use Existing Tool** option
	- Browse a catalog of pre-defined devices cards.
- **Create New Tool** option
	- Name
	- Brewing method
## Add Recipe
**When visible:** After clicking “Add Recipe.”
- **Select Tools:** Dropdown from the user’s saved tools, plus an “Add New Tool” button.
- **Coffee:** name, processing method and region
- **Grind** in ticks or microns
- **Water temperature** in Celsius
- **Pour Steps:** a repeatable form to enter pour weight and pour time

## Add Score Sheet
**When visible:** After clicking “Add Score Sheet” on a recipe that has none
- **Score Sheet Form:** Mirrors the official Brewers Cup evaluation form (aroma, flavor, acidity, body, finish, overall)
