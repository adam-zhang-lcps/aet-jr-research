import {
  StyleSheet,
  View,
  Text,
  Image,
  Dimensions,
  TouchableOpacity,
  ScrollView,
  Linking,
} from "react-native";
import yelp from "../api/yelp.js";
import { useState, useEffect } from "react";
import Carousel from "react-native-reanimated-carousel";
import openMap from "react-native-open-maps";

const HorizontalLine = () => {
  return (
    <View
      style={{
        borderBottomColor: "black",
        borderBottomWidth: 1,
        marginVertical: 4,
      }}
    />
  );
};

const Review = ({ review }) => {
  return (
    <View style={styles.reviewContainer}>
      <View style={styles.reviewHeader}>
        <View>
          <Text style={styles.reviewName}>{review.user.name}</Text>
          <Text>{review.time_created}</Text>
        </View>
        <Text style={styles.reviewStars}>{"⭐".repeat(review.rating)}</Text>
      </View>
      <Text style={styles.reviewText}>{review.text}</Text>
    </View>
  );
};

const YelpBusinessDetails = ({ navigation }) => {
  // Why do we pass `distance` as a prop? Well, according to the Yelp API, the
  // distance is optionally returned "in meters from the search location".
  // Except that the details endpoint doesn't let you *specify* a search
  // location, so it just never fucking returns anything. So we have to keep the
  // one from the search screen. *Sigh*.
  let { businessId, distance } = navigation.state.params;
  const dimension = Dimensions.get("window");

  const [business, setBusiness] = useState(null);
  useEffect(() => {
    (async () => {
      const response = await yelp.get(`/${businessId}`);
      setBusiness(response.data);
    })();
  }, []);

  const [reviews, setReviews] = useState([]);
  useEffect(() => {
    (async () => {
      const response = await yelp.get(`/${businessId}/reviews`);
      setReviews(response.data.reviews);
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
  const call = () => {
    Linking.openURL(`tel:${business.phone}`);
  };

  return (
    <View style={styles.parent}>
      <ScrollView contentContainerStyle={styles.container}>
        <Text style={styles.title}>{business.name}</Text>
        <View style={styles.infoContainer}>
          <View style={styles.iconContainer}>
            <Text style={styles.icon}>⭐</Text>
            <Text style={styles.rating}>{business.rating.toFixed(1)}</Text>
          </View>
          <Text style={styles.reviewCount}>
            ({business.review_count} reviews)
          </Text>
        </View>
        <Carousel
          data={business.photos}
          renderItem={renderPhoto}
          style={styles.carousel}
          autoPlay={true}
          autoPlayInterval={1000}
          width={dimension.width}
          height={0.4 * dimension.height}
        />
        <TouchableOpacity style={styles.infoContainer} onPress={goto}>
          <View style={styles.iconContainer}>
            <Text style={styles.icon}>📍</Text>
            <Text style={styles.location}>{business.location.address1}</Text>
          </View>
          <Text style={styles.distance}>{distance}mi</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.infoContainer} onPress={call}>
          <View style={styles.iconContainer}>
            <Text style={styles.icon}>📞</Text>
            <Text style={styles.location}>{business.phone}</Text>
          </View>
        </TouchableOpacity>
        <View style={styles.reviews}>
          {reviews
            .map((review) => {
              return <Review key={review.id} review={review} />;
            })
            .flatMap((e, index) => [e, <HorizontalLine key={index} />]) // Me when there's no easy way to intersperse in JS
            .slice(0, -1)}
        </View>
      </ScrollView>
      <TouchableOpacity onPress={goto} style={styles.goto}>
        <Text style={styles.distance}>Go</Text>
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  parent: {
    flex: 1,
    flexDirection: "column",
    justifyContent: "center",
    alignItems: "center",
    backgroundColor: "#F0EEEE",
  },
  container: {
    flexDirection: "column",
    alignItems: "stretch",
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
    marginVertical: 10,
    justifyContent: "center",
    backgroundColor: "pink",
  },
  image: {
    width: "100%",
    height: "100%",
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
  reviews: {
    marginTop: 18,
  },
  reviewContainer: {
    marginVertical: 8,
    flexDirection: "column",
  },
  reviewHeader: {
    flexDirection: "row",
    alignItems: "center",
  },
  reviewName: {
    fontWeight: "bold",
    fontSize: 18,
    marginRight: 10,
  },
  reviewStars: {
    marginLeft: "auto",
    alignSelf: "center",
  },
  reviewText: {
    fontSize: 16,
  },
  goto: {
    margin: 10,
    width: "90%",
    backgroundColor: "lightblue",
    padding: 10,
    borderRadius: 16,
  },
});

export default YelpBusinessDetails;
