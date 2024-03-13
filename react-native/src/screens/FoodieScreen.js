import React, { useState } from "react";
import { Text, StyleSheet, View, Button, FlatList } from "react-native";
import SearchBar from "../components/SearchBar";
import yelp from "../api/yelp";
import YelpBusinessPreview from "../components/YelpBusinessPreview";

const FoodieScreen = ({ navigation }) => {
  const [results, setResults] = useState([]);
  const [errMessage, setErrMessage] = useState("");

  const makeYelpRequest = async (term) => {
    try {
      const response = await yelp.get("/search", {
        params: {
          limit: 20,
          term,
          location: "leesburg va",
        },
      });

      console.log(response.data.businesses);

      setResults(response.data.businesses);
    } catch (err) {
      console.log(err);
      setErrMessage("Something went wrong");
    }
  };

  return (
    <View>
      {errMessage ? <Text>{errMessage}</Text> : null}
      <SearchBar onSubmit={makeYelpRequest} />
      <FlatList
        data={results}
        keyExtractor={(result) => result.id}
        renderItem={({ item }) => {
          return <YelpBusinessPreview business={item} />;
        }}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  text: {
    fontSize: 30,
  },
});

export default FoodieScreen;
