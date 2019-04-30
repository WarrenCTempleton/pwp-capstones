dbug_param = False

test_text = "Where did you go, friend? We nearly saw each other. Go forth my friend!"
test_text_2 = "Where art thou my friend? I nearly saw the other friend go forth!"
murder_note = "You may call me heartless, a killer, a monster, a murderer, but I'm still NOTHING compared to the villian that Jay was. This whole contest was a sham, an elaborate plot to shame the contestants and feed Jay's massive, massive ego. SURE you think you know him! You've seen him smiling for the cameras, laughing, joking, telling stories, waving his money around like a prop but off camera he was a sinister beast, a cruel cruel taskmaster, he treated all of us like slaves, like cattle, like animals! Do you remember Lindsay, she was the first to go, he called her such horrible things that she cried all night, keeping up all up, crying, crying, and more crying, he broke her with his words. I miss my former cast members, all of them very much. And we had to live with him, live in his home, live in his power, deal with his crazy demands. AND FOR WHAT! DID YOU KNOW THAT THE PRIZE ISN'T REAL? He never intended to marry one of us! The carrot on the stick was gone, all that was left was stick, he told us last night that we were all a terrible terrible disappointment and none of us would ever amount to anything, and that regardless of who won the contest he would never speak to any of us again! It's definitely the things like this you can feel in your gut how wrong he is! Well I showed him, he got what he deserved all right, I showed him, I showed him the person I am! I wasn't going to be pushed around any longer, and I wasn't going to let him go on pretending that he was some saint when all he was was a sick sick twisted man who deserved every bit of what he got. The fans need to know, Jay Stacksby is a vile amalgamation of all things evil and bad and the world is a better place without him."

myrtle_beech_intro = "Salutations. My name? Myrtle. Myrtle Beech. I am a woman of simple tastes. I enjoy reading, thinking, and doing my taxes. I entered this competition because I want a serious relationship. I want a commitment. The last man I dated was too whimsical. He wanted to go on dates that had no plan. No end goal. Sometimes we would just end up wandering the streets after dinner. He called it a 'walk'. A 'walk' with no destination. Can you imagine? I like every action I take to have a measurable effect. When I see a movie, I like to walk away with insights that I did not have before. When I take a bike ride, there better be a worthy destination at the end of the bike path. Jay seems frivolous at times. This worries me. However, it is my staunch belief that one does not make and keep money without having a modicum of discipline. As such, I am hopeful. I will now list three things I cannot live without. Water. Emery boards. Dogs. Thank you for the opportunity to introduce myself. I look forward to the competition."
lily_trebuchet_intro = "Hi, I'm Lily Trebuchet from East Egg, Long Island. I love cats, hiking, and curling up under a warm blanket with a book. So they gave this little questionnaire to use for our bios so lets get started. What are some of my least favorite household chores? Dishes, oh yes it's definitely the dishes, I just hate doing them, don't you? Who is your favorite actor and why? Hmm, that's a hard one, but I think recently I'll have to go with Michael B. Jordan, every bit of that man is handsome, HANDSOME! Do you remember seeing him shirtless? I can't believe what he does for the cameras! Okay okay next question, what is your perfect date? Well it starts with a nice dinner at a delicious but small restaurant, you know like one of those places where the owner is in the back and comes out to talk to you and ask you how your meal was. My favorite form of art? Another hard one, but I think I'll have to go with music, music you can feel in your whole body and it is electrifying and best of all, you can dance to it! Okay final question, let's see, What are three things you cannot live without? Well first off, my beautiful, beautiful cat Jerry, he is my heart and spirit animal. Second is pasta, definitely pasta, and the third I think is my family, I love all of them very much and they support me in everything I do. I know Jay Stacksby is a handsome man and all of us want to be the first to walk down the aisle with him, but I think he might truly be the one for me. Okay that's it for the bio, I hope you have fun watching the show!"
gregg_t_fishy_intro = "A good day to you all, I am Gregg T Fishy, of the Fishy Enterprise fortune. I am 37 years young. An adventurous spirit and I've never lost my sense of childlike wonder. I do love to be in the backyard gardening and I have the most extraordinary time when I'm fishing. Fishing for what, you might ask? Why, fishing for compliments of course! I have a stunning pair of radiant blue eyes. They will pierce the soul of anyone who dare gaze upon my countenance. I quite enjoy going on long jaunts through garden paths and short walks through greenhouses. I hope that Jay will be as absolutely interesting as he appears on the television. I find that he has some of the most curious tastes in style and humor. When I'm out and about I quite enjoy hearing tales that instill in my heart of hearts the fascination that beguiles my every day life. Every fiber of my being scintillates and vascillates with extreme pleasure during one of these charming anecdotes and significantly pleases my beautiful personage. I cannot wait to enjoy being on A Brand New Jay. It certainly seems like a grand time to explore life and love."

def get_average_sentence_length(text_block):
    text_block = text_block.replace('!', '.') #replace ! with .
    text_block = text_block.replace('?', '.') #replace ? with .
    text_block = text_block.replace('. ', '.') #replace all sentence end with . (no space) because spaces = words
    broken_block = text_block.split('.')
    sentence_length_list = []
    #break block of text into sentences
    for i in broken_block:
        #only count sentence if it is longer than 1 char
        if len(i) > 0:
            #sentence has words separated by spaces
            broken_sentence = i.split(' ')
            #append word count per sentence to array
            sentence_length_list.append(len(broken_sentence))
    sentence_total = 0
    if dbug_param: print("Broken Sentences: ",broken_block)
    if dbug_param: print("Sentence Length: ",sentence_length_list)
    #add up all the sentence lengths
    for n in range(len(sentence_length_list)):
        sentence_total += int(sentence_length_list[n])
    if dbug_param: print(" Total Words: {t_w}\n Total Sentences: {t_s}\n Average Length: {ave}\n".format(t_w=sentence_total, t_s=len(sentence_length_list), ave=sentence_total / len(sentence_length_list)))
    return sentence_total / len(sentence_length_list)

def prepare_text(raw_text):
    delimeter_list = ['.', '?', '!', ',']
    for n in delimeter_list:
        raw_text = raw_text.replace(n,"")
    raw_text = raw_text.lower()
    raw_text = raw_text.split(' ')
    return raw_text

def build_frequency_table(corpus):
    frequency_table = {}
    #Iterate over corpus and add to frequency table
    for i in corpus:
        #i is the word in the corpus
        if frequency_table.get(i) == None:
            frequency_table.update({i:1})
        else:
            count = frequency_table.get(i)
            frequency_table.update({i:count+1})
    return frequency_table

def ngram_creator(text_list):
    #receive prepared text, create tupples list
    ngram_list = []
    for n in range(len(text_list)):
        #first word does not have a tupple
        if n > 1:
            ngram_instance = str(text_list[n-1]+" "+text_list[n])
            ngram_list.append(ngram_instance)
    return ngram_list

def frequency_comparison(table1, table2):
    #table 1 and table 2 are frequency tables
    appearances = {}
    mutual_appearances = {}
    if dbug_param: print("Table 1: ", table1)
    if dbug_param: print("Table 2: ", table2)
    #iterate over table 1, check if elements are 
    #in table 2. If so, add to mutual_appearances
    #else, just add elements to appearances
    for key in table1.keys():
        table1_freq = table1.get(key)
        table2_freq = table2.get(key)
        if table2_freq == None:
            #Table 2 does not have the item
            appearances.update({key:table1_freq})
        else:
            #Table 2 DOES have the item
            #The smaller value gets added to mutual,
            #the larger value to appearances 
            if table1_freq > table2_freq:
                appearances.update({key:table1_freq})
                mutual_appearances.update({key:table2_freq})
            elif table2_freq > table1_freq:
                appearances.update({key:table2_freq})
                mutual_appearances.update({key:table1_freq})
            elif table2_freq == table1_freq:
                appearances.update({key:table1_freq})
                mutual_appearances.update({key:table1_freq})
            else:
                #This should never happen
                print("ERROR")
    for key in table2.keys():
        #Iterate through table 2, 
        #add only elements in table 2, not in appearances
        if appearances.get(key) == None:
            appearances.update({key:table2.get(key)})
    if dbug_param: print("MUTUAL LIST: ", mutual_appearances)
    if dbug_param: print("APPEARANCES LIST", appearances)
    mutual_total = 0
    appearances_total = 0
    for i in mutual_appearances.values():
        mutual_total += int(i)
    for n in appearances.values():
        appearances_total += int(n)
    
    if dbug_param: print("MUTUAL: ",mutual_total)
    if dbug_param: print("TOTAL APPEAR: ",appearances_total)
    return mutual_total / appearances_total

def percent_difference(value1, value2):
    return (abs(value1-value2)/((value1 + value2)/2))

def find_text_similarity(sample1, sample2):
    #Find Difference in Sentence Lengths
    print("######Similarity between {author1} and {author2}####".format(author1=sample1.author, author2=sample2.author))
    sentence_length_difference = percent_difference(sample1.average_sentence_length, sample2.average_sentence_length)
    sentence_length_similarity = abs(1-sentence_length_difference)
    print("Similarity - sentence length:", sentence_length_similarity)
    word_count_simliarity = frequency_comparison(sample1.word_count_frequency, sample2.word_count_frequency)
    print("Similarity - word count:", word_count_simliarity)
    ngram_similarity = frequency_comparison(sample1.ngram_frequency, sample2.ngram_frequency)
    print("Similarity - ngram:", ngram_similarity)
    print("Similarity - blended score:", (sentence_length_similarity + word_count_simliarity + ngram_similarity)/3)
    print("################")
    return (sentence_length_similarity + word_count_simliarity + ngram_similarity)/3

class TextSample():
    def __init__(self, text, author):
        self.raw_text = text
        self.author = author
        self.average_sentence_length = get_average_sentence_length(self.raw_text)    
        self.prepared_text = prepare_text(text)
        self.word_count_frequency = build_frequency_table(self.prepared_text)
        self.ngram_frequency = build_frequency_table(ngram_creator(self.prepared_text))
    def __repr__(self):
        return "{author} writes with an average sentence length {length}".format(author=self.author, length=self.average_sentence_length)

#####TEST CONTENT#####
test_text_sample_A = TextSample(test_text, "Warren")
test_text_sample_B = TextSample(test_text_2, "Evil Warren")
#print(test_text_sample)
#print(prepare_text(test_text))
#print(build_frequency_table(prepare_text(test_text)))
#warren_text_1 = (ngram_creator(prepare_text(test_text)))
#warren_text_2 = (ngram_creator(prepare_text(test_text_2)))
#warren_text_1 = build_frequency_table(warren_text_1)
#warren_text_2 = build_frequency_table(warren_text_2)
#print(frequency_comparison(warren_text_1,warren_text_2))
print("DIFF: ", percent_difference(180,120))
startup_check = find_text_similarity(test_text_sample_A,test_text_sample_B)


###ASSIGNMENT SCRIPT#####
murderer_sample = TextSample(murder_note, "murderer")
lily_sample = TextSample(lily_trebuchet_intro, "Lily")
myrtle_sample = TextSample(myrtle_beech_intro, "Myrtle")
gregg_sample = TextSample(gregg_t_fishy_intro, "Gregg")

print(murderer_sample)
print(lily_sample)
print(myrtle_sample)
print(gregg_sample)

def compare_authors(sample_author_text):
    author_score = find_text_similarity(murderer_sample, sample_author_text)
    print("{author} scored a similarity of {score} with the murderer\n".format(author=sample_author_text.author, score=author_score))
    return author_score

compare_authors(murderer_sample)

scores = {}
scores.update({"Lily":compare_authors(lily_sample)})
scores.update({"Myrtle":compare_authors(myrtle_sample)})
scores.update({"Gregg":compare_authors(gregg_sample)})

max_score = max(scores.values())
for n in scores.keys():
    if scores.get(n) == max_score:
        print("{author} is the most likely killer with score {score}\n".format(author=n, score=scores.get(n)))
