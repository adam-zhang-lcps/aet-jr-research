import { View, Image, Text, TouchableOpacity, StyleSheet } from "react-native";

const CounterDetail = ({ imageSource, onIncrease, count }) => {
  return (
    <View style={styles.container}>
      <TouchableOpacity onPress={onIncrease}>
        <Image source={imageSource} style={styles.image} />
      </TouchableOpacity>

      <View style={styles.infoContainer}>
        <Text style={styles.text}>{count}</Text>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flexDirection: "row",
    flexBasis: 200,
  },
  image: {
    aspectRatio: 1,
    flex: 1,
    resizeMode: "cover",
    alignSelf: "stretch",
  },
  infoContainer: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
  },
  text: {
    fontSize: 64,
  },
});

export default CounterDetail;
