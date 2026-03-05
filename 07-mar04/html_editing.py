# Last time modified: 05/03/26 (Canadian Style)
# Author: Anthony
# html edition Assignment

def My_website():

    # Read base HTML
    with open("Base.html", "r") as website:
        html_base = website.read()

    # Update PageTitle
    page_title = "The A.I. Python Website"
    html_modified = html_base.replace("<title>Document</title>", f"<title>{page_title}</title>")

    # Insert DaisyUI
    daisy_ui = """
    <!-- Daisy UI -->
    <link href="https://cdn.jsdelivr.net/npm/daisyui@5" rel="stylesheet" type="text/css" />
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
    <link href="https://cdn.jsdelivr.net/npm/daisyui@5/themes.css" rel="stylesheet" type="text/css" />
    """

    html_modified = html_modified.replace("</head>", daisy_ui + "\n</head>")

    # Theme
    theme = "Vaporwave"
    html_modified = html_modified.replace('<html lang="en">', f'<html lang="en" data-theme="{theme}">')

    # Navbar
    nav_bar = """
    <div class="navbar bg-base-100 shadow-sm">
      <a class="btn btn-ghost text-xl">daisyUI</a>
    </div>
    """

    # Hero
    my_Hero = """
    <div class="hero bg-base-200 min-h-screen">
      <div class="hero-content flex-col lg:flex-row-reverse">
        <img src="https://img.daisyui.com/images/stock/photo-1635805737707-575885ab0820.webp"
             class="max-w-sm rounded-lg shadow-2xl" />
        <div>
          <h1 class="text-5xl font-bold">Box Office News!</h1>
          <p class="py-6">
            Provident cupiditate voluptatem et in. Quaerat fugiat ut assumenda excepturi exercitationem quasi.
          </p>
          <button class="btn btn-primary">Get Started</button>
        </div>
      </div>
    </div>
    """

    # List
    my_List = """
    <ul class="list bg-base-100 rounded-box shadow-md">
      ...
    </ul>
    """

    # Insert components
    html_modified = html_modified.replace('<body>', '<body>\n' + nav_bar)
    html_modified = html_modified.replace('</body>', my_Hero + my_List + "\n</body>")

    # Write output
    with open("index.html", "w") as file:
        file.write(html_modified)


# Run the function
My_website()