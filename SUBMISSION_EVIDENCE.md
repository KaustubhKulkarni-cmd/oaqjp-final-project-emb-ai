# Assessment evidence checklist

Use these commands in the Coursera lab from `/home/project/final_project`. Save the actual output in the named evidence files and paste it into the corresponding assessment answer. Do not use fabricated output.

- `2b_application_creation`: interactive-shell import/function output and test command output.
- `3a_output_formatting`: formatted `emotion_detection.py` source.
- `3b_formatted_output_test`: output from printing the formatted dictionary.
- `4b_packaging_test`: output from importing `EmotionDetection.emotion_detection`.
- `5a_unit_testing`: source of `test_emotion_detection.py`.
- `5b_unit_testing_result`: actual successful unit-test output.
- `6a_server`: source of `server.py`.
- `6b_deployment_test.png`: screenshot of the running app with text and detected emotions.
- `7a_error_handling_function`: source of the updated packaged emotion detector.
- `7b_error_handling_server`: source of `server.py` showing blank-input handling.
- `7c_error_handling_interface.png`: real screenshot showing blank-input error handling.
- `8a_server_modified`: final `server.py` source used for static analysis.
- `8b_static_code_analysis`: actual Pylint output.

Useful commands:
```bash
python3 -m unittest -v test_emotion_detection.py
python3 server.py
python3 -m pylint server.py
```

For package validation:
```bash
python3 -c "from EmotionDetection.emotion_detection import emotion_detector; print(emotion_detector('I am very angry'))"
```

For the formatted output:
```bash
python3 -c "from EmotionDetection.emotion_detection import emotion_detector; print(emotion_detector('I am really mad about this'))"
```
