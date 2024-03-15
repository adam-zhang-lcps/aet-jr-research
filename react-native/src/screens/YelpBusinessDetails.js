import {
  StyleSheet,
  View,
  Text,
  Image,
  Dimensions,
  TouchableOpacity,
} from "react-native";
import yelp from "../api/yelp.js";
import { useState, useEffect } from "react";
import Carousel from "react-native-reanimated-carousel";
import openMap from "react-native-open-maps";

const YelpBusinessDetails = ({ navigation }) => {
  let { businessId } = navigation.state.params;
  const dimension = Dimensions.get("window");

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

  const renderPhoto = ({ item }) => {
    return (
      <Image style={styles.image} source={{ uri: item }} resizeMode="cover" />
    );
  };
  const goto = () => {
    openMap({
      end: `${business.coordinates.latitude},${business.coordinates.longitude}`,
    });
  };

  return (
    <View style={styles.container}>
      <View style={styles.infoContainer}>
        <Text style={styles.title}>{business.name}</Text>
        <Text style={styles.price}>{business.price}</Text>
      </View>
      <Carousel
        data={business.photos}
        renderItem={renderPhoto}
        style={styles.carousel}
        autoPlay={true}
        autoPlayInterval={1000}
        width={dimension.width}
        height={0.3 * dimension.height}
      />
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
        {business.distance && (
          <Text style={styles.distance}>{Math.round(business.distance)}m</Text>
        )}
      </View>
      <View style={styles.infoContainer}>
        <View style={styles.iconContainer}>
          <Text style={styles.icon}>📞</Text>
          <Text style={styles.location}>{business.phone}</Text>
        </View>
      </View>
      <TouchableOpacity onPress={goto} style={styles.goto}>
        <Text style={styles.distance}>Go</Text>
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    flexDirection: "column",
    alignItems: "stretch",
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
  carousel: {
    width: "100%",
    justifyContent: "center",
    backgroundColor: "pink",
  },
  image: {
    width: "100%",
    height: "100%",
    borderRadius: 16,
    backgroundColor: "pink",
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
    alignSelf: "center",
  },
  reviewCount: {
    fontSize: 16,
    alignSelf: "center",
  },
  location: {
    fontSize: 18,
    alignSelf: "center",
  },
  distance: {
    fontSize: 16,
    alignSelf: "center",
  },
  goto: {
    backgroundColor: "lightblue",
    padding: 10,
    borderRadius: 16,
    width: "100%",
    marginTop: "auto",
  },
});

export default YelpBusinessDetails;
