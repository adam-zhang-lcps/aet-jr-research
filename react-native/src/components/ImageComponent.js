import { Image, Text, View } from "react-native";

const styles = {
  container: {
    flexDirection: "row",
  },
  image: {
    aspectRatio: 1,
    flex: 1,
    resizeMode: "cover",
  },
  infoContainer: {
    flex: 1,
    flexDirection: "column",
    justifyContent: "center",
  },
  title: {
    fontSize: 30,
    textAlign: "center",
  },
  author: {
    fontSize: 20,
    textAlign: "center",
    backgroundColor: "lightblue",
  },
};

const ImageComponent = (props) => {
  return (
    <View style={styles.container}>
      <Image source={props.source} style={styles.image} />
      <View style={styles.infoContainer}>
        <Text style={styles.title}>{props.title}</Text>
        <Text style={styles.author}>{props.author}</Text>
      </View>
    </View>
  );
};

export default ImageComponent;
