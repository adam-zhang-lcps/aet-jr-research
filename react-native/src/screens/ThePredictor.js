import React, { useState } from "react";
import {
  Text,
  StyleSheet,
  View,
  TextInput,
  Button,
  ImageBackground,
} from "react-native";

const ThePredictor = () => {
  /*
   * text is the current text being entered by the user
   * displayText is the question that corresponds to prediction
   */
  const [text, setText] = useState("");
  const [displayText, setDisplayText] = useState("");
  const [prediction, setPrediction] = useState("");
  /*
   * Defining a list variable
   * to do: add more predictions to the list
   */
  const [predictionList, setPredictionList] = useState([
    "Yes, it will come true",
    "Not in your wildest dreams",
    "Perhaps soon",
    "Patience is a virtue",
  ]);

  /*
   * called when the user enters a character.   The character is appended to newText by RN
   * the console.log() will display on your terminal
   */
  const setQuestion = (newText) => {
    setText(newText);

    console.log("setQuestion: " + newText);
  };

  /*
   * Called when the user presses the "get prediction" button
   * to do:
   *         Use Math.floor and Math.random() to select a random prediction in your predictionList
   *         Clear out the current question in the text box
   */
  const updateScreen = () => {
    setDisplayText(text);
    setPrediction(
      predictionList[Math.floor(Math.random() * predictionList.length)],
    );
    setQuestion("");
  };
  const image = {
    uri: "https://legacy.reactjs.org/logo-og.png",
  };

  return (
    <View style={styles.container}>
      <View style={styles.titleBlock}>
        <Text style={styles.titleText}>The Predictor</Text>
      </View>
      <View style={styles.firstBlock}>
        <Text style={styles.questionText}>Question: </Text>
        <TextInput
          style={styles.textInput}
          placeholder="enter your question here"
          onChangeText={(newText) => setQuestion(newText)}
          defaultValue={text}
        />
        <Button onPress={updateScreen} title="get Prediction" color="#841584" />
      </View>
      <View style={styles.secondBlock}>
        <ImageBackground source={image} resizeMode="cover" style={styles.image}>
          <Text style={styles.predictionText}>{displayText}</Text>
          <Text style={styles.predictionText}> </Text>
          <Text style={styles.predictionText}>{prediction}</Text>
        </ImageBackground>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    backgroundColor: "yellow",
    justifyContent: "space-between",
    flex: 1,
  },
  titleBlock: {
    backgroundColor: "black",
    flex: 1,
  },
  firstBlock: {
    backgroundColor: "gray",
    flex: 2,
  },
  secondBlock: {
    backgroundColor: "white",
    flex: 6,
  },
  titleText: {
    color: "red",
    fontSize: 40,
    textAlign: "center",
  },
  textInput: {
    backgroundColor: "white",
    color: "black",
    height: 40,
    fontSize: 20,
  },
  questionText: {
    color: "blue",
    fontSize: 35,
    textAlign: "center",
  },
  predictionText: {
    color: "orange",
    fontSize: 50,
    fontWeight: "bold",
    textAlign: "center",
  },
  image: {
    justifyContent: "center",
    flex: 1,
  },
});

export default ThePredictor;
