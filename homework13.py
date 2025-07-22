import bs4
from gtts import gTTS

def extract_stories_from_NPR_text(text):
    '''
    Extract a list of stories from the text of the npr.com webpage.
    
    @params: 
    text (string): the text of a webpage
    
    @returns:
    stories (list of tuples of strings): a list of the news stories in the web page.
      Each story should be a tuple of (title, teaser), where the title and teaser are
      both strings.  If the story has no teaser, its teaser should be an empty string.
    '''
    soup = bs4.BeautifulSoup(text, 'html.parser')
    stories = []
    
    # Find all story elements - NPR stories are typically in div with class 'story-text'
    story_divs = soup.find_all('div', class_='story-text')
    
    for div in story_divs:
        # Extract title from h3 with class 'title'
        title_tag = div.find('h3', class_='title')
        title = title_tag.get_text(strip=True) if title_tag else ""
        
        # Extract teaser from p with class 'teaser'
        teaser_tag = div.find('p', class_='teaser')
        teaser = teaser_tag.get_text(strip=True) if teaser_tag else ""
        
        if title:  # Only include stories with titles
            stories.append((title, teaser))
    
    return stories

def read_nth_story(stories, n, filename):
    '''
    Read the n'th story from a list of stories.
    
    @params:
    stories (list of tuples of strings): a list of the news stories from a web page
    n (int): the index of the story you want me to read
    filename (str): filename in which to store the synthesized audio

    Output: None
    '''
    # Validate input
    if not isinstance(stories, list):
        raise TypeError("stories must be a list")
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0 or n >= len(stories):
        raise IndexError("n is out of range")
    if not isinstance(filename, str):
        raise TypeError("filename must be a string")
    
    # Get the selected story
    title, teaser = stories[n]
    
    # Combine title and teaser with proper punctuation
    text_to_speak = f"{title}. {teaser}" if teaser else title
    
    # Generate and save the audio
    try:
        tts = gTTS(text=text_to_speak, lang='en')
        tts.save(filename)
    except Exception as e:
        raise RuntimeError(f"Failed to generate audio: {str(e)}")
