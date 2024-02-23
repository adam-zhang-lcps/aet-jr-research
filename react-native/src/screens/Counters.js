import React, { useState } from "react";
import { Text, StyleSheet, View } from "react-native";
import CounterDetail from "../components/CounterDetail";

const Counters = () => {
  const programmingLanguages = [
    {
      name: "JavaScript",
      image: require("../../assets/javascript.png"),
    },
    {
      name: "Rust",
      image: require("../../assets/rust.png"),
    },
    {
      name: "C",
      image: require("../../assets/c.png"),
    },
  ];
  const state = {};
  for (const language of programmingLanguages) {
    const [count, setCount] = useState(0);
    state[language.name] = { count, setCount };
  }

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Favorite Programming Language</Text>
      {programmingLanguages.map((language) => {
        const { name, image } = language;
        const { count, setCount } = state[name];
        return (
          <CounterDetail
            key={name}
            imageSource={image}
            onIncrease={() => setCount(count + 1)}
            count={count}
          />
        );
      })}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flexDirection: "column",
  },
  title: {
    fontSize: 36,
    textAlign: "center",
  },
});

export default Counters;
