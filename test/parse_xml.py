import xml.etree.ElementTree as ET
import os
# import os
#
# directory = 'xml_logs'
# count = 0
#
# for folder_1 in os.listdir('xml_logs'):
#     if folder_1.startswith('s01') or folder_1.startswith('.DS_Store'):
#         continue
#     sub_dir1 = os.path.join(directory, folder_1)
#     # print(sub_dir1)
#     for folder_2 in os.listdir(sub_dir1):
#         if folder_2.startswith("medium"):
#             sub_dir2 = os.path.join(sub_dir1, folder_2)
#             # print(sub_dir2)
#             for file in os.listdir(sub_dir2):
#                 count += 1
#
#                 # print("{} -> {} -> {}".format(sub_dir1, sub_dir2, file))
# print("The number of files that were encountered is {}".format(count))

# class XMLParsingData:
#     def makeList(self, currentDirectory, user, gesture, gestureTypes):
#         tempTemplate = []
#
#         currentDirectory += "/xml_logs/" + user + "/medium/";
#         temp = currentDirectory
#         for g in gesture:
#             for gt in gestureTypes:
#                 temp += g + gt + ".xml"
#                 tempTemplate.append(loadTemplates(temp))
#                 temp = currentDirectory
#         return tempTemplate
#     def fullGestureList(self):
#         currentDirectory = os.getcwd()
#         users = ["s02", "s03", "s04", "s05", "s06", "s07", "s08", "s09", "s10", "s11"]
#         gesture = ["arrow", "caret", "check", "circle", "delete_mark", "left_curly_brace", "left_sq_bracket","pigtail",
#                    "question_mark", "rectangle", "right_curly_brace", "star", "triangle", "v", "x"]
#         gesture_types = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10"]
#
#         gesForUser = []
#         g = []
#
#         for u in users:
#             user = u
#             gesForUser = self.makeList(currentDirectory, user, gesture, gesture_types)
#


# public class XMLParsingData {
#
#     public ArrayList<GesStructure> makeArraylist(String currentDirectory, String user, String[] gesture,
#                                                  String[] gesturesTypes) throws ParserConfigurationException, SAXException, IOException {
#         ArrayList<GesStructure> tempTemplate = new ArrayList<>();
#         currentDirectory += "/xml_logs/" + user + "/medium/";
#         String temp = currentDirectory;
#         for (String g : gesture) {
#             for (String gt : gesturesTypes) {
#                 temp += g + gt + ".xml";
#                 tempTemplate.add(loadTemplates(temp));
#                 temp = currentDirectory;
#             }
#         }
#         return tempTemplate;
#     }
#
#     public ArrayList<GestureStructure> fullGestureList() throws ParserConfigurationException, IOException, SAXException {
#         String currentDirectory = System.getProperty("user.dir");
#         String user;
#         String[] users = { "s02", "s03", "s04", "s05", "s06", "s07", "s08", "s09", "s10", "s11" };
#         String[] gesture = { "arrow", "caret", "check", "circle", "delete_mark", "left_curly_brace", "left_sq_bracket",
#                 "pigtail",
#                 "question_mark", "rectangle", "right_curly_brace", "star", "triangle", "v", "x" };
#         String[] gesturesTypes = { "01", "02", "03", "04", "05", "06", "07", "08", "09", "10" };
#         ArrayList<GesStructure> gesForUser;
#         ArrayList<GestureStructure> g = new ArrayList<>();
#         for (String u : users) {
#             user = u;
#             gesForUser = makeArraylist(currentDirectory, user, gesture, gesturesTypes);
#             g.add(new GestureStructure(user, gesForUser));
#         }
#         for (GestureStructure ges : g) {
#             System.out.println("User: " + ges.user + " Template Size: " + ges.Template.size());
#         }
#         return g;
#     }
#
#     public GesStructure loadTemplates(String filename)
#             throws ParserConfigurationException, SAXException, IOException {
#         Document doc = xmlparser(filename);
#         Element root = doc.getDocumentElement();
#         String l = root.getAttribute("Name");
#         l = l.substring(0, l.length() - 2);
#         GesStructure g = new GesStructure();
#         g.label = l;
#         // Get a list of all the elements with the tag name "log"
#         NodeList nodeList = doc.getElementsByTagName("Point");
#         ArrayList<PointClass> p = new ArrayList<>();
#         PointClass pt = new PointClass();
#
#         // Loop through the list and print the content of each element
#         for (int temp = 0; temp < nodeList.getLength(); temp++) {
#
#             Node node = nodeList.item(temp);
#
#             if (node.getNodeType() == Node.ELEMENT_NODE) {
#
#                 Element element = (Element) node;
#                 String s1 = element.getAttribute("X");
#                 String s2 = element.getAttribute("Y");
#                 pt.x = Integer.parseInt(s1);
#                 pt.y = Integer.parseInt(s2);
#                 p.add(pt);
#             }
#         }
#         Template t = new Template(l, p);
#         g.points = t.Points;
#         return g;
#     }
#
#     public Document xmlparser(String filepath) throws ParserConfigurationException, SAXException, IOException {
#         File file = new File(filepath);
#         DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
#         DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
#         Document doc = dBuilder.parse(file);
#
#         // Normalize the document
#         doc.getDocumentElement().normalize();
#         return doc;
#     }
#
#
# }

# public class

from ast import Set
import os
from sys import platform
import xml.etree.ElementTree as ET
from collections import OrderedDict

from numpy import mean
from recognition import Point
from recognition import Recognizer
# from random import choices
import random
from templates import Template,Unistroke
import csv

recognizer = Recognizer()

print(platform)

cwd = os.getcwd() + '/xml_logs'
print(cwd)

dataset = []

dataDict = {}
gestureList = []
for folderName in os.listdir(cwd):
    if folderName.startswith('.DS_Store'):
        continue

    userFolder = cwd + '/' + folderName
    speedFolder = userFolder + '/medium'
    gestureList = []
    gestureMap = {}
    for xml in os.listdir(speedFolder):

        xml = speedFolder + '/' + xml
        tree = ET.parse(xml)
        root = tree.getroot()
        name = root.attrib.get('Name')[:-2]
        subject = root.attrib.get('Subject')
        speed = root.attrib.get('Speed')
        number = int(root.attrib.get('Number'))
        numpts = root.attrib.get('NumPts')
        points = []

        for i in range(0, len(root)):
            x = int(root[i].attrib.get('X'))
            y = int(root[i].attrib.get('Y'))
            # point_list = []
            # point_list.append(x)
            # point_list.append(y)
            points.append((x,y))
        if name in gestureMap:
            gestureMap[name][number] = points
        else:
            gestureMap[name] = {}
            gestureMap[name][number] = points

        # gestureMap[name] = points
        gestureMap = OrderedDict(sorted(dict.items(gestureMap)))
    dataDict[folderName] = gestureMap
# print((dataDict['s05']['caret'][1]))
# print("$$$$$$$$$$$$$$$$$$$")
# print(len(dataDict['s05']['caret'][1]))
#
# print("################")

for user in dataDict.keys():
    for gesture in dataDict[user].keys():
        for number in dataDict[user][gesture].keys():
            current_point_list = dataDict[user][gesture][number]
            dataDict[user][gesture][number] = recognizer.preprocess(current_point_list)

# print(dataDict['s05']['caret'][1])
# print("$$$$$$$$$$$$$$$$$")
# print(len(dataDict['s05']['caret'][1]))

with open("gesture_logs.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["User", "GestureType", "IterationNumber", "#TrainingExamples", "TrainingSetSize", "TrainingSetContents",
                     "Candidate", "RecoResultGestureType", "Correct/Incorrect", "RecoResultScore", "RecoResultBestMatch",
                     "RecoResultNBestSorted"])

    total_correct_count = 0
    total_count = 0

    for U in dataDict.keys():
        print("U ------------- : {}".format(U))


        for E in range(1, 2):
            recognition_score = 0

            for i in range(1, 2):
                templatelist = []
                candidatelist = []

                training_set_contents = ""
                for gesture in dataDict[U].keys():
                    templatelistnumberlist = random.sample(range(1,11), E)
                    candidatelistnumber = random.sample(list(set([i for i in range(1,11)]) - set(templatelistnumberlist)), 1)[0]
                    for number in templatelistnumberlist:
                        new_template = Unistroke(gesture, list(dataDict[U][gesture][number]), U, number)
                        templatelist.append(new_template)
                        training_set_contents += "{}-{}-{}:::".format(U, new_template.name, number)
                    new_candidate = Unistroke(gesture, dataDict[U][gesture][candidatelistnumber], U, candidatelistnumber)
                    candidatelist.append(new_candidate)
                recognizer = Recognizer()
                training_set_contents = ""
                for template in templatelist:
                    # print(template.name)
                    # print(template.points)

                    recognizer.addGesture(template)
                correct_recognitions = 0


                for candidate in candidatelist:
                    total_count += 1
                    row = []
                    # print(candidate)
                    # print()
                    matched_gesture, score, n_best_list = recognizer.recognize_with_nbest_list(candidate.points)
                    user = U
                    gesture_type = candidate.name
                    iteration_number = i
                    number_of_training_examples = E
                    total_training_set_size = E * 16
                    current_candidate = "{}-{}-{}".format(U, gesture_type, candidate.example_count)
                    recognition_result = matched_gesture.name
                    recognition_correct = 0
                    recognition_result_score = score
                    n_best_list_string = ""
                    matched_template_string = "{}-{}-{}".format(matched_gesture.user, matched_gesture.name, matched_gesture.example_count)
                    for entry in n_best_list:
                        n_best_list_string += "{}-{}-{}-{}:::".format(entry[0], entry[1], entry[2], entry[3])


                    if matched_gesture.name == candidate.name:
                        total_correct_count += 1
                        recognition_correct = 1
                        correct_recognitions += 1
                    row.append(user)
                    row.append(gesture_type)
                    row.append(iteration_number)
                    row.append(number_of_training_examples)
                    row.append(total_training_set_size)
                    row.append(training_set_contents)
                    row.append(current_candidate)
                    row.append(recognition_result)
                    row.append(recognition_correct)
                    row.append(recognition_result_score)
                    row.append(matched_template_string)
                    row.append(n_best_list_string)
                    writer.writerow(row)


                recognition_score += (correct_recognitions/ len(candidatelist))

            # recognition_score /= 10

            print("Recognition score for User : {}, E value : {} is {}".format(U, E, recognition_score))


    total_average_accuracy = total_correct_count/total_count
    print("The total average accuracy is : {}".format(total_average_accuracy))
    row = []
    row.append("Total Average Accuracy")
    row.append(total_average_accuracy)
    writer.writerow(row)





# GestureType = ["triangle", "x", "rectangle", "circle", "check", "caret",
#                  "arrow", "left_sq_bracket", "right_sq_bracket", "v", "delete_mark", "left_curly_brace", "right_curly_brace", "star", "pigtail", "question_mark"]
#
# for U in dataDict.keys():
#     scoreList = []
#     print("U, ---------------", U)
#     for E in range(1, 3):
#         print("E, ---------------", E)
#         # Add 1-100 loop
#         recoScore = 0
#         scoreList = []
#         TemplateSet = []
#         TempTest = []
#         TempTestLabels = []
#         TestSet = []
#         TestSetLabels = []
#         PickedLabels = []
#         for G in GestureType:
#             recoScore = 0
#             PickGestureList = []
#             for key in dataDict[U].keys():
#                 if (G in key):
#                     PickGestureList.append(recognizer.Unistroke(key, dataDict[U][key]))
#
#                     TempTest.append(recognizer.Unistroke(key, dataDict[U][key]))
#
#             for p in range(1, E + 1):
#
#                 randIndexTemplate = random.randint(0, len(PickGestureList) - 1)
#
#                 TemplateSet.append(PickGestureList[randIndexTemplate])
#
#                 for t in TempTest:
#                     if t.Name == PickGestureList[randIndexTemplate].Name:
#                         TempTest.remove(t)
#
#             randIndexTest = random.randint(0, len(TempTest) - 1)
#             TestSet.append(TempTest[randIndexTest])
#
#             for T in TestSet:
#                 # print("To be tested ",T[0])
#                 Points = recognizer.resample(points=T.Points, n=64)
#                 # print("points ",len(Points))
#                 r = recognizer.indicativeAngle(Points)
#                 Points = recognizer.rotateBy(Points, r)
#                 Points = recognizer.scaleTo(Points, recognizer.SquareSize)
#                 Points = recognizer.translateTo(Points, recognizer.Origin)
#                 # print("points ",len(Points))
#                 resName = recognizer.recognize(points=Points, templates=TemplateSet, size=recognizer.SquareSize)
#                 print("Original ", T.Name, "Res ", resName[0].Name, resName[1], resName[2], "Match",
#                       resName[0].Name[:-2] == T.Name[:-2])
#                 if resName[0].Name[:-2] == T.Name[:-2]:
#                     recoScore += 1
#                 # print("SCore for ", G, recoScore, "out of", len(TestSet))
#                 scoreList.append(recoScore)
#
#         # scoreList.append(recoScore/100)
#     print("Avg Score for User", U, ":", mean(scoreList))


# cwd = os.getcwd() + '\Project1' + '\\' + 'xml' + '\\xml_logs'
