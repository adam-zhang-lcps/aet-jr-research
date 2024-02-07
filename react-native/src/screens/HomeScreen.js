import React from "react";
import { View, Button, Text, StyleSheet } from "react-native";

const HomeScreen = (props) => {
  const navigation = props.navigation;
  return (
    <View>
      <Text style={styles.text}>HomeScreen</Text>
      <View>
        <Text style={styles.text}>Hi there!</Text>
        <Button
          onPress={() => navigation.navigate("SongListScreen")}
          title="Go to SongList"
        />
        <Button
          onPress={() => navigation.navigate("CuteScreen")}
          title="Go to CuteAnimals"
        />
        <Button
          onPress={() => navigation.navigate("Counter")}
          title="Go to Counter"
        />
        <Button
          onPress={() => navigation.navigate("StylingBoxScreen")}
          title="Go to StylingBoxScreen"
        />
        <Button
          onPress={() => navigation.navigate("NorwayFlag")}
          title="Go to NorwayFlag"
        />
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  text: {
    fontSize: 30,
  },
});

export default HomeScreen;
