import pandas
import csv


# df = pandas.read_csv('data.csv')
# print(df["Name"])
# print(df[1])

# for i in range(1,86):


def main():

    matches = []
    totalrows = 121

    with open('data.csv', newline='') as csvfile:

        reader = csv.DictReader(csvfile)
        mainReader = reader


        print(reader)
        dat = list(reader)

        for current in dat:
            print("a")
            score = [0] * totalrows

            lookingFor = current['I am looking for']
            date = current['My perfect first date is....']
            importance = current['What is most important to you in your potential match?']
            placeToStudy = current['Favorite place to study on campus?']
            fitness = current['How important is fitness to you?']
            pineApple = current['Pineapple on pizza? ']
            datingApp = current['Do you use dating apps?']
            fridayNight = current['Ideal Friday night']
            spiritAnimal = current['My spirit animal is ']
            favMeal = current['Favorite meal']
            social = current['Favorite social media']

            gender = current['I am a...']
            gender_desired = current['Looking for a...']

            it = 0
            print("a")
            for future in dat:
                if future['Paid'] == 'Pending':
                    continue
                # Making sure they are not the same person
                if current['Name'] == future["Name"]:
                    continue

                # Matching the genders
                if future['I am a...'] != current['Looking for a...']:
                    continue

                if future['Looking for a...'] != current['I am a...']:
                    continue

                if current['I preferred to be matched with...'] == 'Someone in my year':
                    if current['What year are you?'] == future['What year are you?']:
                        score[int(future['Index'])] += 5


                if future['I am looking for'] == lookingFor:
                    score[int(future['Index'])] += 3

                if future['My perfect first date is....'] == date:
                    score[int(future['Index'])] += 2

                if future['What is most important to you in your potential match?'] == importance:
                    score[int(future['Index'])] += 1

                if future['Favorite place to study on campus?'] == placeToStudy:
                    score[int(future['Index'])] += 1

                if future['Looking for a...'] == fitness:
                    score[int(future['Index'])] += 1

                if future['Pineapple on pizza? '] == pineApple:
                    score[int(future['Index'])] += 1

                if future['Do you use dating apps?'] == datingApp:
                    score[int(future['Index'])] += 1

                if future['Ideal Friday night'] == fridayNight:
                    score[int(future['Index'])] += 1

                if future['My spirit animal is '] == spiritAnimal:
                    score[int(future['Index'])] += 1

                if future['Favorite meal'] == favMeal:
                    score[int(future['Index'])] += 1

                if future['Favorite social media'] == social:
                    score[int(future['Index'])] += 1

            z = sorted(range(len(score)), key=lambda i: score[i])[-3:]
            print(z)
            if current['By submitting my answers, I agree to Venmo @Bronco-Match. I understand that I will only receive my potential Bronco match and/or detailed results if I pay and that all proceeds go to charity.  '] == 'Yes I agree to pay $2 for the name of my match':
                matches.append((dat[z[0]]['Name'] +" " + dat[z[0]]['(Optional) Write your social media accounts'],
                                dat[z[1]]['Name'] + " " +dat[z[1]]['(Optional) Write your social media accounts'],
                                dat[z[2]]['Name'] + " " + dat[z[2]]['(Optional) Write your social media accounts']))
            else:
                matches.append([dat[z[0]],dat[z[1]],dat[z[2]]])



            # matches.append(score)

    print("___________________________________________")
    for x in matches:
        print(x)

    #print(matches[1])
    # max_id = matches[4].index(max(matches[4]))
    # print("Name", dat[18])
    # # print(max_id)
    # #print(dat[max_id])
    # z = sorted(range(len(matches[18])), key=lambda i: matches[18][i])[-3:]
    # print(z)
    # print(dat[z[0]])
    # print(dat[z[1]])
    # print(dat[z[2]]['Name'])
    # with open('results.csv', mode='w') as result_csv:
    #     result_csv = csv.writer(result_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #     result_csv.writeRow([])

# for i in range(totalrows):
    #     max_id = matches[i].index(max(matches[i]))
    #     top_3 = sorted(range(len(matches[i])), key=lambda x: matches[i][x])[-3:]
    #


if __name__== "__main__" :
    main()