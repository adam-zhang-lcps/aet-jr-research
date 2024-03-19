import { StyleSheet, View, Text, Image, TouchableOpacity } from "react-native";

const MILES_PER_METER = 0.0006213712;

const YelpBusinessPreview = ({ business, navigation }) => {
  const distance = Math.round(business.distance * MILES_PER_METER);

  return (
    <TouchableOpacity
      onPress={() =>
        navigation.navigate("YelpBusinessDetails", {
          businessId: business.id,
          distance,
        })
      }
      style={styles.container}
    >
      <Image source={{ uri: business.image_url }} style={styles.image} />
      <Text style={styles.title}>{business.name}</Text>
      <View style={styles.infoContainer}>
        <Text style={styles.rating}>
          <Text>⭐</Text>
          {business.rating.toFixed(1)}
        </Text>
        <Text>({business.review_count} reviews)</Text>
      </View>
      <View style={styles.infoContainer}>
        <Text>
          <Text>📍</Text> {business.location.address1}
        </Text>
        <Text>{distance}mi</Text>
      </View>
    </TouchableOpacity>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    minWidth: 300,
    backgroundColor: "#F0EEEE",
    margin: 10,
    borderRadius: 16,
    padding: 10,
  },
  image: {
    width: "100%",
    height: 200,
    borderRadius: 16,
  },
  title: {
    fontSize: 24,
    fontWeight: "bold",
  },
  infoContainer: {
    flexDirection: "row",
    justifyContent: "space-between",
  },
  rating: {
    fontSize: 16,
    fontWeight: "bold",
  },
});

export default YelpBusinessPreview;
