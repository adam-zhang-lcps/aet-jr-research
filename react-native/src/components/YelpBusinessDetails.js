import { StyleSheet, View, Text, Image } from "react-native";
import yelp from "../api/yelp.js";
import { useState, useEffect } from "react";

const YelpBusinessDetails = ({ navigation }) => {
  let { businessId } = navigation.state.params;

  const [business, setBusiness] = useState(null);
  useEffect(() => {
    (async () => {
      const response = await yelp.get(`/${businessId}`);
      setBusiness(response.data);
    })();
  }, []);

  if (!business) {
    return null;
  }

  return (
    <View style={styles.container}>
      <View style={styles.infoContainer}>
        <Text style={styles.title}>{business.name}</Text>
        <Text style={styles.price}>{business.price}</Text>
      </View>
      <Image source={{ uri: business.image_url }} style={styles.image} />
      <View style={styles.infoContainer}>
        <View style={styles.iconContainer}>
          <Text style={styles.icon}>⭐</Text>
          <Text style={styles.rating}>{business.rating.toFixed(1)}</Text>
        </View>
        <Text style={styles.reviewCount}>
          ({business.review_count} reviews)
        </Text>
      </View>
      <View style={styles.infoContainer}>
        <View style={styles.iconContainer}>
          <Text style={styles.icon}>📍</Text>
          <Text style={styles.location}>{business.location.address1}</Text>
        </View>
        <Text style={styles.distance}>{Math.round(business.distance)}m</Text>
      </View>
      <View style={styles.infoContainer}>
        <View style={styles.iconContainer}>
          <Text style={styles.icon}>📞</Text>
          <Text style={styles.location}>{business.phone}</Text>
        </View>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#F0EEEE",
    margin: 10,
    borderRadius: 16,
    padding: 10,
  },
  title: {
    fontSize: 48,
    fontWeight: "bold",
  },
  price: {
    fontSize: 24,
    alignSelf: "center",
  },
  image: {
    width: "100%",
    height: "40%",
    resizeMode: "cover",
    borderRadius: 16,
  },
  infoContainer: {
    flexDirection: "row",
    justifyContent: "space-between",
  },
  iconContainer: {
    flexDirection: "row",
  },
  icon: {
    fontSize: 24,
  },
  rating: {
    fontSize: 18,
    fontWeight: "bold",
  },
  reviewCount: {
    fontSize: 16,
    alignSelf: "center",
  },
  location: {
    fontSize: 18,
  },
  distance: {
    fontSize: 16,
    alignSelf: "center",
  },
});

export default YelpBusinessDetails;
