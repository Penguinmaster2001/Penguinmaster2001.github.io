# Rust HTML Generator Test

Small Rust program that can generate HTML web pages.

## HTML Page Structure

- **Page**

  Contains top level elements.

  head: Head

  header: Header

  body: Body

  footer: Footer

### Top Level Elements

- **Head**

  Metadata for the page

  - Title
  - Charset
  - Scaling
  - Style linking
  - Favicon

- **Header**

    :Top of the page, can contain elements

- **Body**

  Main page content, can contain elements

- **Footer**

  Bottom of the page, can contain elements

### Elements

- **Text**

  Type:

  - Header

    Size: 1 - 6

  - Paragraph
  - Code

  Content: String

  > Can contain html elements inside such as `<i>`, `<s>`, `<a>`, `<b>`, etc.

- **Styled Text**

  > For building text with style tags.

- **Linking and Embedding**

  - Link

    Link: String

  - Image

    Path: String

- **Sectioning**

  Type:

  - Article
  - Aside
  - Div
  - Main
  - Nav
  - Ordered List
  - Section
  - Unordered List

  Content: Collection of Elements

- **Other**

  - Raw HTML

    html: String

Class: String (optional)

> For CSS styling
