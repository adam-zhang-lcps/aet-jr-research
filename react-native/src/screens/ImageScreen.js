import { Text } from "react-native";
import ImageComponent from "../components/ImageComponent";
import { ScrollView } from "react-native-gesture-handler";

const styles = {
  title: {
    fontSize: 36,
    fontWeight: "bold",
    textAlign: "center",
  },
};

const ImageScreen = () => {
  const paintings = [
    {
      title: "American Gothic",
      author: "Grant Wood",
      source: require("../../assets/AmericanGothic.jpg"),
    },
    {
      title: "The Scream",
      author: "Edvard Munch",
      source: require("../../assets/TheScream.jpg"),
    },
    {
      title: "Starry Night",
      author: "Vincent Van Gogh",
      source: require("../../assets/StarryNight.jpg"),
    },
    {
      title: "Mona Lisa",
      author: "Leonardo Da Vinci",
      source: require("../../assets/MonaLisa.jpg"),
    },
  ];
  return (
    <ScrollView>
      <Text style={styles.title}>Famous Paintings</Text>
      {paintings.map((painting, index) => (
        <ImageComponent
          key={index}
          title={painting.title}
          author={painting.author}
          source={painting.source}
        />
      ))}
    </ScrollView>
  );
};

export default ImageScreen;
