import { StyleSheet, View, Text, Image, TouchableOpacity } from "react-native";

const YelpBusinessPreview = ({ business, navigation }) => {
  return (
    <TouchableOpacity
      onPress={() =>
        navigation.navigate("YelpBusinessDetails", { businessId: business.id })
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
        <Text>{Math.round(business.distance)}m</Text>
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
