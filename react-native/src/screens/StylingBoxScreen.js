import React, { useState } from "react";
import { Text, StyleSheet, View, Button } from "react-native";

const StylingBoxScreen = () => {
  return (
    <View style={styles.container}>
      <View style={styles.horizontalContainer}>
        <View style={styles.horizontal} />
      </View>
      <View style={styles.vertical} />
      <View style={styles.horizontalContainer}>
        <View style={styles.horizontal} />
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    backgroundColor: "#256aa2",
    width: "100%",
    height: "100%",
    flexDirection: "row",
  },
  horizontal: {
    backgroundColor: "#f8cc46",
    height: "13%",
  },
  vertical: {
    backgroundColor: "#f8cc46",
    width: "10%",
    flexGrow: 1,
  },
  horizontalContainer: {
    flexGrow: 2,
    justifyContent: "center",
  },
});

export default StylingBoxScreen;
