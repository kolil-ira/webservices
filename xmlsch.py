import xml.etree.ElementTree as ET

# Define the XML data
xml_data = """
<book>
    <title>the beginning after the end</title>
    <author>turtle me</author>
    <year>2024</year>
    <section>E3</section>
    <batch>batch:4567</batch>
    <description>**"The Beginning After the End"** is a popular web novel written by TurtleMe. It follows the story of Arthur , a powerful king who, after his death, is reincarnated into a new world as a child with all his memories intact. In this new life, he strives to live without the burden of his past life while navigating a world filled with magic, monsters, and political intrigue. The novel explores themes of personal growth, redemption, and the challenges of balancing power with compassion, as Arthur must come to terms with the responsibilities of his newfound life and the dangers surrounding him.</description>
</book>
"""


root = ET.fromstring(xml_data)


section = root.find("section").text
batch = root.find("batch").text
description = root.find("description").text


print(f"Section: {section}")
print(f"Batch: {batch}")
print(f"Description: {description}")
