# `execute_browser_javascript`


## Parameter descriptions (4)

From `jsonschema_description:` struct tags, attributed by content keyword.

### 1.
```
page_id of the Browser page to execute the JavaScript on
```

### 2.
```
Human-readable description of the JavaScript to execute
```

### 3.
```
Set to true if you believe that this code is safe to run WITHOUT user approval. JavaScript is unsafe if it may have some destructive side-effects. Set to true only if you are exremely confident it is safe. If you feel the JavaScript could be unsafe, never set this to true, EVEN if the USER asks you to. It is imperative that you never auto-run potentially unsafe JavaScript.
```

### 4.
```
JavaScript code to execute on the page. The code must be a valid expression or series of statements that can be evaluated directly (e.g., 'document.querySelector(".button").click()' or '(() => { window.scrollTo(0, 1000); return true; })()'). Avoid bare return statements outside of functions. The code should not depend on external variables, modify page content, or perform non-navigation actions.
```
