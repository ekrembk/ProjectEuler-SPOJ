#ProjectEuler problem 22
#Solved: 16 Jun 2016
#NOTE: For this program to work, a text file named "p022_names.txt" is needed in the same directory
#as this code file which is provided in the ProjectEuler webpage for the problem 22

def recognize_letter(character): #function for recognizing a single character
	letters_dict = { #dictionary for letters
		'A' : 1,
		'B' : 2,
		'C' : 3,
		'D' : 4,
		'E' : 5,
		'F' : 6,
		'G' : 7,
		'H' : 8,
		'I' : 9,
		'J' : 10,
		'K' : 11,
		'L' : 12,
		'M' : 13,
		'N' : 14,
		'O' : 15,
		'P' : 16,
		'Q' : 17,
		'R' : 18,
		'S' : 19,
		'T' : 20,
		'U' : 21,
		'V' : 22,
		'W' : 23,
		'X' : 24,
		'Y' : 25,
		'Z' : 26}
	return letters_dict[character]

def main():
    fo = open('p022_names.txt','r')
    text = fo.read()
    fo.close()
    p_text = ''
    for c in text:
        if c != '"':
            if c == ',':
                p_text += ' '
            else:
                p_text += c
    p_text = sorted(p_text.split())
    final_sum = 0

    counter = 0
    for name in p_text:
        counter += 1
        total = 0
        for character in name:
            total += recognize_letter(character)
        final_sum += counter*total
    print final_sum

if __name__ == '__main__':
        main()
