import React, { useState } from "react";
import { Text, StyleSheet, View, Button } from "react-native";

const NorwayFlag = () => {
  return (
    <View style={styles.container}>
      <View style={styles.verticalContainer}>
        <View style={styles.topLeft} />
        <View style={styles.vertical} />
        <View style={styles.topRight} />
      </View>
      <View style={styles.horizontal} />
      <View style={styles.verticalContainer}>
        <View style={styles.bottomLeft} />
        <View style={styles.vertical} />
        <View style={styles.bottomRight} />
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    backgroundColor: "white",
    width: "100%",
    height: "40%",
    flexDirection: "column",
  },
  horizontal: {
    backgroundColor: "#00205b",
    flexGrow: 1,
  },
  vertical: {
    backgroundColor: "#00205b",
    flexGrow: 1,
  },
  verticalContainer: {
    flexDirection: "row",
    flexGrow: 3,
  },
  topLeft: {
    backgroundColor: "#ba0c2f",
    flexGrow: 2,
    borderRightWidth: 20,
    borderBottomWidth: 20,
    borderColor: "white",
  },
  topRight: {
    backgroundColor: "#ba0c2f",
    flexGrow: 5,
    borderLeftWidth: 20,
    borderBottomWidth: 20,
    borderColor: "white",
  },
  bottomLeft: {
    backgroundColor: "#ba0c2f",
    flexGrow: 2,
    borderTopWidth: 20,
    borderRightWidth: 20,
    borderColor: "white",
  },
  bottomRight: {
    backgroundColor: "#ba0c2f",
    flexGrow: 5,
    borderTopWidth: 20,
    borderLeftWidth: 20,
    borderColor: "white",
  },
});

export default NorwayFlag;
