Xian Chen

CS477 HW#1

September 10th 2013


```
**Purpose**

The purpose of this experiment is to use regular expressions to extract proper nouns from two different commencement speeches and one BBC news article and use it to determine the most important concepts or ideas that the speaker/author is trying to convey. 
```


```
**The Motivation**

Proper nouns make up every event, idea, or concept. They are identifiers like logos and carry companies, people, ideas, and so much more. For example, before the majority of the population knew what Edward Snowden did, they knew his name. In the spoken and written language repetition is often used to emphasize something important. Highly recognizable and highly used proper nouns signify importance. Therefore by identifying the proper nouns and the frequency in which they are used in some linguistic context it should be easy to isolate the idea or concept of the highest importance as well as get a general idea of what it is about.
```


```
**The Experiment**

I used the following regular expression to extract the proper nouns in JFK’s commencement speech at the American University in 1963, Steve Jobs’ commencement speech at Stanford University in 2005 and Jason Palmer’s BBC news article.

[A-Za-z]\s+([A-Z][a-z]+(\s*[A-Z][a-z]+)*


At first I wanted to write a regular expression to extract all nouns rather than just proper nouns but there was not a clear way to do so, since in English, nouns do not follow a specific pattern. As a result, I resolved to write a regular expression for proper nouns. My first attempt at writing one was:

\b([A-Z][a-z]+)\b

The above regular expression finds all words that start off with a capital letter and are followed by one or more lowercase letters. I quickly realized that this method, when used to run regexm.py, generates a lot of errors because along with proper nouns, it also extracts words at the beginning of sentences. This expression does however find all proper nouns. I decided to improve this regex and the result was the following:

[^.”\s*]\s+([A-Z][a-z]+\b)

This expression produced fewer errors, for it filtered out words that appear in the beginning of sentences. Nevertheless I was still unsatisfied with the numbers of errors it made. For instance, it did not handle proper nouns like “United States” as one word. Therefore, I rewrote the expression as:

[^.”\s*]\s+([A-Z][a-z]+(\s*[A-Z][a-z]+)*)

The above expression solved cases like “United States” but it still made errors with words beginning with a capital letter and appearing in the middle of a sentences-- especially those that follow symbols like a single quote ( ‘ ). Resolving all these cases would require the addition of too many exceptions in the [^.”.....\s*] clause at the beginning of the regex. As a result I modified the regex as follows:

[A-Za-z]\s+([A-Z][a-z]+(\s*[A-Z][a-z]+)*

This is the final expression I wrote to find proper nouns. The problem with this regex is that it only extracts proper nouns that appear in the middle of sentences and ignores proper nouns that appear in the beginning. Since the regex is impartial to what it ignores, I will be assuming that the ratios at which the proper nouns appear in comparison to each other with this regex is the same as when the regex is perfect.
```


```
**The Findings**

Using regexcount3.py along with the regular expression for proper nouns that I have written, I was able to find the frequency in which each proper noun appears in the two commencement speeches and the BBC news article. I hypothesized that just by looking at the proper nouns of the highest frequencies I can figure out the main idea/topic of the two speeches and the news article. 


From running regexcount3.py alon with my proper noun regular expression on JFK’s commencement speech (http://www.jfklibrary.org/Asset-Viewer/BWC7I4C9QUmLG9J6I8oy8w.aspx) I received the following:

[(9, 'Soviet Union'), (4, 'United States'), (4, 'Nation'), (4, 'Americans'), (4, 'American'), (3, 'Communist'), (2, 'Soviets'), (2, 'Soviet'), (2, 'Second World War'), (2, 'Moscow'), (2, 'Geneva'), (1, 'Woodrow Wilson'), (1, 'Western Europe'), (1, 'Western'), (1, 'West New Guinea'), (1, 'West Berlin'), (1, 'Washington'), (1, 'United Nations'), (1, 'Scriptures'), (1, 'Russian'), (1, 'President Woodrow Wilson'), (1, 'Peace Corps'), (1, 'Pax Americana'), (1, 'Our'), (1, 'National Service Corps'), (1, 'National'), (1, 'Minister Macmillan'), (1, 'Military Strategy')...]


Just by looking at the first two most frequent proper nouns extracted by the program I can assume that the main concern in JFK’s 1963 American University Commencement Speech was the Cold War. If I were to look at the following 8 most frequent words, I could further corroborate this assumption. To further back up my hypothesis, I reviewed the article myself and confirmed the accuracy of my claim.


Similarly, taking the top 10 most frequent proper nouns extracted from Steve Jobs’ 2005 Stanford University Commencement speech (http://news.stanford.edu/news/2005/june15/jobs-061505.html) I can assume that Apple was the main topic of interest (Apple was the most frequently used word with a count of 8 followed by Mac/Macintosh with a count of 4). 


To further test my hypothesis, I ran the same test on a BBC article on the Higgs boson (http://www.bbc.co.uk/news/science-environment-21785205). The most frequently occurring proper noun generated was: Higgs-- showing up 14 times. 
```


I hypothesized that the proper noun that shows up at the highest frequency in any linguistic context is the main constituent of the idea or concept of the highest importance. It can therefore, like a logo representing a company, represent the entire linguistic context. Using the regular expression I created, [A-Za-z]\s+([A-Z][a-z]+(\s*[A-Z][a-z]+)*, I extracted the proper nouns on two commencement speeches as well as a BBC article on the Higgs boson. In all three cases the proper noun that appeared at the highest frequency correctly represented its associated context.
