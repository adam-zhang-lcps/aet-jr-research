import React, { useState } from "react";
import { Text, StyleSheet, View, FlatList } from "react-native";
import SearchBar from "../components/SearchBar";
import yelp from "../api/yelp";
import YelpBusinessPreview from "../components/YelpBusinessPreview";

const FoodieScreen = ({ navigation }) => {
  const [results, setResults] = useState("");
  const [errMessage, setErrMessage] = useState("");

  const makeYelpRequest = async (term) => {
    setErrMessage(null);

    try {
      const response = await yelp.get("/search", {
        params: {
          limit: 20,
          term,
          location: "leesburg va",
        },
      });

      setResults(response.data.businesses);
    } catch (err) {
      console.error(err);
      setErrMessage("Something went wrong");
    }
  };

  // Pre-populate (this is definitely not how to do this, but it works ¯\_(ツ)_/¯)
  // if (!results && !errMessage) {
  //   makeYelpRequest("");
  // }

  return (
    <View>
      {errMessage ? <Text>{errMessage}</Text> : null}
      <SearchBar onSubmit={makeYelpRequest} />
      <FlatList
        data={results}
        keyExtractor={(result) => result.id}
        renderItem={({ item }) => {
          return (
            <YelpBusinessPreview business={item} navigation={navigation} />
          );
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
