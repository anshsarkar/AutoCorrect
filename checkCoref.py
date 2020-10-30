import spacy
import neuralcoref

nlp = spacy.load("en_core_web_md")

text = "The mitochondrion is a double membrane bound organelle found in most eukaryotic organisms. Some cells in some multicellular organisms may however lack them. A number of unicellular organisms have transformed this into other structures. They are also known as the powerhouse of the cell. They take in nutrients breaks then down and creates energy rick molecules for the cells. The biochemical processes of the cell are known as cellular respiration"

greedyness = [0.2, 0.4, 0.5, 0.6, 0.8, 1]
max_dist = [20, 50, 75, 100, 150]
max_dist_match = [250, 500, 750, 1000]

for g in greedyness:
    for md in max_dist:
        for mdm in max_dist_match:
            neuralcoref.add_to_pipe(nlp, max_dist=md, greedyness=g, max_dist_match=mdm)
            doc = nlp(text)
            print(doc._.coref_resolved)
            nlp.remove_pipe("neuralcoref")

