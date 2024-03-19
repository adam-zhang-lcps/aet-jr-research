import React, { useEffect, useState } from "react";
import { Text, StyleSheet, View, FlatList, ScrollView } from "react-native";
import SearchBar from "../components/SearchBar";
import yelp from "../api/yelp";
import YelpBusinessPreview from "../components/YelpBusinessPreview";

const ScrollableRow = ({ title, businesses }) => {
  return (
    <View>
      <Text style={styles.text}>{title}</Text>
      <FlatList
        horizontal
        data={businesses}
        keyExtractor={(result) => result.id}
        renderItem={({ item }) => {
          return <YelpBusinessPreview business={item} />;
        }}
      />
    </View>
  );
};

const FoodieScreen = ({ navigation }) => {
  const [costEffective, setCostEffective] = useState("");
  const [moreExpensive, setMoreExpensive] = useState("");
  const [asian, setAsian] = useState("");
  const [errMessage, setErrMessage] = useState("");

  const makeYelpRequest = async (params, set) => {
    setErrMessage(null);

    try {
      const response = await yelp.get("/search", {
        params: {
          limit: 20,
          location: "leesburg va",
          ...params,
        },
      });

      set(response.data.businesses);
    } catch (err) {
      console.error(err);
      setErrMessage("Something went wrong");
    }
  };

  // What the f*cking hell, React?
  // This is the recommended way to fetch data on component mount with async/await
  useEffect(() => {
    (async () => {
      await makeYelpRequest({ price: 1 }, setCostEffective);
      await makeYelpRequest({ price: "3,4" }, setMoreExpensive);
      await makeYelpRequest({ categories: ["asianfusion"] }, setAsian);
    })();
  }, []);

  return (
    <View>
      {errMessage ? <Text>{errMessage}</Text> : null}
      <SearchBar onSubmit={makeYelpRequest} />
      <ScrollView>
        <ScrollableRow title="Cost Effective" businesses={costEffective} />
        <ScrollableRow title="More Expensive" businesses={moreExpensive} />
        <ScrollableRow title="Asian" businesses={asian} />
      </ScrollView>
    </View>
  );
};

const styles = StyleSheet.create({
  text: {
    fontSize: 30,
  },
});

export default FoodieScreen;
