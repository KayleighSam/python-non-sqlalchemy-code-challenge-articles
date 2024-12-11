class Article:
    # Class variable to store all articles created
    all_articles = []

    def __init__(self, author, magazine, title):
        # Input validation
        if not isinstance(author, Author) or not isinstance(magazine, Magazine) or not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Invalid author, magazine, or title")
        
        # Assign values to instance variables
        self._author = author
        self._magazine = magazine
        self._title = title
        
        # Add the article to the global list of articles 
        Article.all_articles.append(self)
        author._articles.append(self)
        magazine._articles.append(self)

  # Property methods to access the attributes
    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    @classmethod
    def all(cls):
        return cls.all_articles  # Return the list of all articles


class Author:
    def __init__(self, name):
        
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        
        self._name = name
        self._articles = []     

    # Property method to access the author's name
    @property
    def name(self):
        return self._name

    # Method to retrieve all articles written by the author
    def articles(self):
        return self._articles

    # Method to get all unique magazines the author has written for
    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    # Method to add an article for the author
    def add_article(self, magazine, title):
        return Article(self, magazine, title)  # Create and return a new article

  
    def topic_areas(self):
        topic_areas = {article.magazine.category for article in self._articles}
        return list(topic_areas) if topic_areas else None


class Magazine:
    _all_magazines = []  # Class-level list to store all Magazine instances

    def __init__(self, name, category):
        # Validate that the magazine name and category are correct
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Magazine name must be a string between 2 and 16 characters")
        if not isinstance(category, str) or not category:
            raise ValueError("Category must be a non-empty string")
        
        self._name = name
        self._category = category
        self._articles = [] 
        Magazine._all_magazines.append(self)  
        # Class method to retrieve all magazines
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Magazine name must be between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("Category must be a non-empty string")
        self._category = value

        
    def articles(self):
        return self._articles

    # Method to get all unique authors who have contributed to the magazine
    def contributors(self):
        return list({article.author for article in self._articles})  # Unique authors

    # Method to get the titles of all articles in the magazine
    def article_titles(self):
        return [article.title for article in self._articles] if self._articles else None

    # Method to add an article to the magazine
    def add_article(self, author, title):
        # Validate author and title
        if not isinstance(author, Author) or not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Invalid author or title")
        
        # Create and add the article to the magazine
        article = Article(author, self, title)
        self._articles.append(article)
        return article

    #  get authors who have contributed more than 2 articles
    def contributing_authors(self):
        author_counts = {}
        for article in self.articles():
            author = article.author
            author_counts[author] = author_counts.get(author, 0) + 1

        # Filter authors with more than 2 articles in this magazine
        authors_with_multiple_articles = [author for author, count in author_counts.items() if count > 2]
        return authors_with_multiple_articles if authors_with_multiple_articles else None

# Create instances of authors and magazines
author_1 = Author("Carry Bradshaw")
author_2 = Author("Nathaniel Hawthorne")
magazine_1 = Magazine("Vogue", "Fashion")
magazine_2 = Magazine("AD", "Architecture")

# Create articles
Article(author_1, magazine_1, "How to wear a tutu with style")
Article(author_1, magazine_1, "How to be single and happy")
Article(author_1, magazine_1, "Dating life in NYC")
Article(author_1, magazine_2, "Carrara Marble is so 2020")
Article(author_2, magazine_2, "2023 Eccentric Design Trends")

# Print articles written by each author
print("Articles by each author:")
for author in [author_1, author_2]:
    print(f"Author: {author.name}")
    if author.articles():
        for article in author.articles():
            print(f"  - {article.title} (Magazine: {article.magazine.name})")
    else:
        print("  No articles written.")
    print()

# Print articles published in each magazine
print("Articles in each magazine:")
for magazine in [magazine_1, magazine_2]:
    print(f"Magazine: {magazine.name} (Category: {magazine.category})")
    if magazine.articles():
        for article in magazine.articles():
            print(f"  - {article.title} (Author: {article.author.name})")
    else:
        print("  No articles published.")
    print()


