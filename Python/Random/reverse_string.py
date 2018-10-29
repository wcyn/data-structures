def reverse(text):
    print(f"Text: {text}")
    if len(text) <= 1:
        return text

    return reverse(text[1:]) + text[0]

print(reverse("hello there"))