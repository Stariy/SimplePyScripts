#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


import base64
text = b'IyEvdXNyL2Jpbi9lbnYgcHl0aG9uMwojIC0qLSBjb2Rpbmc6IHV0Zi04IC0qLQoKX19hdXRob3JfXyA9ICdpcGV0cmFzaCcKCgojIHVybCA9ICdodHRwOi8vb3BlbmRhdGEubWtyZi5ydS9vcGVuZGF0YS83NzA1ODUxMzMxLXJlZ2lzdGVyX21vdmllcy9kYXRhLTE2LXN0cnVjdHVyZS0zLmpzb24nCiMKIyBpbXBvcnQgcmVxdWVzdHMKIyBycyA9IHJlcXVlc3RzLmdldCh1cmwpCiMKIyB3aXRoIG9wZW4oJ2RhdGEtMTYtc3RydWN0dXJlLTMuanNvbicsIG1vZGU9J3diJykgYXMgZjoKIyAgICAgZi53cml0ZShycy5jb250ZW50KQoKCkRCX0ZJTEVfTkFNRSA9ICdvcGVuZGF0YV9yZWdpc3Rlcl9tb3ZpZXMuc3FsaXRlJwoKCmRlZiBjcmVhdGVfY29ubmVjdCgpOgogICAgaW1wb3J0IHNxbGl0ZTMKICAgIHJldHVybiBzcWxpdGUzLmNvbm5lY3QoREJfRklMRV9OQU1FKQoKCmRlZiBpbml0X2RiKCk6CiAgICAjINCh0L7Qt9C00LDQvdC40LUg0LHQsNC30Ysg0Lgg0YLQsNCx0LvQuNGG0YsKICAgIGNvbm5lY3QgPSBjcmVhdGVfY29ubmVjdCgpCiAgICB0cnk6CiAgICAgICAgY29ubmVjdC5leGVjdXRlc2NyaXB0KG9wZW4oJ2luaXRfZGJfb3BlbmRhdGFfcmVnaXN0ZXJfbW92aWUuc3FsJykucmVhZCgpKQogICAgICAgIGNvbm5lY3QuY29tbWl0KCkKCiAgICBmaW5hbGx5OgogICAgICAgIGNvbm5lY3QuY2xvc2UoKQoKCmlmIF9fbmFtZV9fID09ICdfX21haW5fXyc6CiAgICBpbml0X2RiKCkKCiAgICBpbXBvcnQganNvbgogICAganNvbl9kYXRhID0ganNvbi5sb2FkKG9wZW4oJ2RhdGEtMTQtc3RydWN0dXJlLTMuanNvbicsICdyJywgZW5jb2Rpbmc9J3V0Zi04JykpCiAgICAjIHByaW50KGxlbihqc29uX2RhdGEpKQogICAgIyBwcmludChqc29uLmR1bXBzKGpzb25fZGF0YVswXSwgaW5kZW50PTQsIGVuc3VyZV9hc2NpaT1GYWxzZSkpCgogICAgIyBsID0gc2V0KCkKICAgIGRlYnVnID0gRmFsc2UKICAgICMgZGVidWcgPSBUcnVlCgogICAgY29ubmVjdCA9IGNyZWF0ZV9jb25uZWN0KCkKCiAgICBmb3IgZmlsbSBpbiBqc29uX2RhdGE6CiAgICAgICAgdHJ5OgogICAgICAgICAgICAjIHByaW50KGZpbG0pCiAgICAgICAgICAgIGluZm8gPSBmaWxtWydkYXRhJ11bJ2dlbmVyYWwnXQoKICAgICAgICAgICAgIyBNb3ZpZS5uYW1lCiAgICAgICAgICAgIG5hbWUgPSBpbmZvLmdldCgnZmlsbW5hbWUnKS5zdHJpcCgpCiAgICAgICAgICAgIGRlYnVnIGFuZCBwcmludCgn0J3QsNC30LLQsNC90LjQtSDRhNC40LvRjNC80LA6JywgbmFtZSkKCiAgICAgICAgICAgICMgTW92aWUuZm9yZWlnbk5hbWUKICAgICAgICAgICAgZm9yZWlnbl9uYW1lID0gaW5mby5nZXQoJ2ZvcmVpZ25OYW1lJykKICAgICAgICAgICAgaWYgZm9yZWlnbl9uYW1lOgogICAgICAgICAgICAgICAgZm9yZWlnbl9uYW1lID0gZm9yZWlnbl9uYW1lLnN0cmlwKCkKICAgICAgICAgICAgICAgIGRlYnVnIGFuZCBwcmludCgn0J3QsNC40LzQtdC90L7QstCw0L3QuNC1INC90LAg0LjQvdC+0YHRgtGA0LDQvdC90L7QvCDRj9C30YvQutC1OicsIGZvcmVpZ25fbmFtZSkKCiAgICAgICAgICAgICMgRGlyZWN0b3IubmFtZQogICAgICAgICAgICAjIExpbmtfTW92aWVfRGlyZWN0b3IuZGlyZWN0b3JfaWQKICAgICAgICAgICAgIyDQoNCw0LfQtNC10LvQtdC9ICIsIiwg0L/QvtGB0LvQtSDRgdC00LXQu9Cw0YLRjCBzdHJpcCAtLSDQvNC+0LPRg9GCINC+0YHRgtCw0YLRjNGB0Y8g0L/RgNC+0LHQtdC70YssINC90LAg0L3QtdC60L7RgtC+0YDRi9GFINC10YHRgtGMICdcbicKICAgICAgICAgICAgZGlyZWN0b3IgPSBpbmZvLmdldCgnZGlyZWN0b3InLCBbXSkKICAgICAgICAgICAgaWYgZGlyZWN0b3I6CiAgICAgICAgICAgICAgICBkaXJlY3RvciA9IFt4LnN0cmlwKCkgZm9yIHggaW4gZGlyZWN0b3Iuc3BsaXQoJywnKV0KICAgICAgICAgICAgICAgIGRlYnVnIGFuZCBwcmludCgn0KDQtdC20LjRgdGB0LXRgCjRiyk6JywgZGlyZWN0b3IpCgogICAgICAgICAgICAjIE1vdmllLmdlbnJlX2lkCiAgICAgICAgICAgICMgR2VucmUubmFtZQogICAgICAgICAgICBnZW5yZSA9IGluZm8uZ2V0KCd2aWV3TW92aWUnKQogICAgICAgICAgICBkZWJ1ZyBhbmQgcHJpbnQoJ9CW0LDQvdGAOicsIGdlbnJlKQoKICAgICAgICAgICAgIyBTdHVkaW8ubmFtZQogICAgICAgICAgICAjIExpbmtfTW92aWVfU3R1ZGlvLnN0dWRpb19pZAogICAgICAgICAgICAjINCg0LDQt9C00LXQu9C10L0gIiwiLCDQv9C+0YHQu9C1INGB0LTQtdC70LDRgtGMIHN0cmlwIC0tINC80L7Qs9GD0YIg0L7RgdGC0LDRgtGM0YHRjyDQv9GA0L7QsdC10LvRiywg0L3QsCDQvdC10LrQvtGC0L7RgNGL0YUg0LXRgdGC0YwgJ1xuJwogICAgICAgICAgICBzdHVkaW8gPSBpbmZvLmdldCgnc3R1ZGlvJywgW10pCiAgICAgICAgICAgIGlmIHN0dWRpbzoKICAgICAgICAgICAgICAgIHN0dWRpbyA9IFt4LnN0cmlwKCkgZm9yIHggaW4gc3R1ZGlvLnNwbGl0KCcsJyldCiAgICAgICAgICAgICAgICBkZWJ1ZyBhbmQgcHJpbnQoJ9Ch0YLRg9C00LjRjy3Qv9GA0L7QuNC30LLQvtC00LjRgtC10LvRjDonLCBzdHVkaW8pCgogICAgICAgICAgICAjIE1vdmllLnllYXJPZlByb2R1Y3Rpb24KICAgICAgICAgICAgeWVhcl9vZl9wcm9kdWN0aW9uID0gaW5mby5nZXQoJ2NyWWVhck9mUHJvZHVjdGlvbicpCiAgICAgICAgICAgIGRlYnVnIGFuZCBwcmludCgn0JPQvtC0INC/0YDQvtC40LfQstC+0LTRgdGC0LLQsDonLCB5ZWFyX29mX3Byb2R1Y3Rpb24pCgogICAgICAgICAgICAjIE1vdmllLm51bWJlck9mU2VyaWVzCiAgICAgICAgICAgIG51bWJlcl9vZl9zZXJpZXMgPSBpbmZvLmdldCgnbnVtYmVyT2ZTZXJpZXMnKQogICAgICAgICAgICBkZWJ1ZyBhbmQgcHJpbnQoJ9Ca0L7Qu9C40YfQtdGB0YLQstC+INGB0LXRgNC40Lk6JywgbnVtYmVyX29mX3NlcmllcykKCiAgICAgICAgICAgICMgTW92aWUuZHVyYXRpb24KICAgICAgICAgICAgZHVyYXRpb24gPSBpbmZvLmdldCgnZHVyYXRpb25NaW51dGUnKQogICAgICAgICAgICBkZWJ1ZyBhbmQgcHJpbnQoJ9Cf0YDQvtC00L7Qu9C20LjRgtC10LvRjNC90L7RgdGC0Ywg0L/QvtC60LDQt9CwLCDQvNC40L3Rg9GC0Ys6JywgZHVyYXRpb24pCgogICAgICAgICAgICAjIE1vdmllLmNvbG9yCiAgICAgICAgICAgIGNvbG9yID0gaW5mb1snY29sb3InXQogICAgICAgICAgICBkZWJ1ZyBhbmQgcHJpbnQoJ9Cm0LLQtdGCOicsIGNvbG9yKQoKICAgICAgICAgICAgIyBBZ2VDYXRlZ29yeS5uYW1lCiAgICAgICAgICAgICMgTW92aWUuYWdlQ2F0ZWdvcnlfaWQKICAgICAgICAgICAgYWdlX2NhdGVnb3J5ID0gaW5mby5nZXQoJ2FnZUNhdGVnb3J5JykKICAgICAgICAgICAgZGVidWcgYW5kIHByaW50KCfQktC+0LfRgNCw0YHRgtC90LDRjyDQutCw0YLQtdCz0L7RgNC40Y8g0LfRgNC40YLQtdC70YzRgdC60L7QuSDQsNGD0LTQuNGC0L7RgNC40Lg6JywgYWdlX2NhdGVnb3J5KQoKICAgICAgICAgICAgIyBNb3ZpZS5hbm5vdGF0aW9uCiAgICAgICAgICAgIGFubm90YXRpb24gPSBpbmZvLmdldCgnYW5ub3RhdGlvbicpCiAgICAgICAgICAgIGRlYnVnIGFuZCBwcmludCgn0JDQvdC90L7RgtCw0YbQuNGPOicsIGFubm90YXRpb24pCgogICAgICAgICAgICAjIENvdW50cnlPZlByb2R1Y3Rpb24ubmFtZQogICAgICAgICAgICAjIExpbmtfTW92aWVfQ291bnRyeU9mUHJvZHVjdGlvbi5jb3VudHJ5T2ZQcm9kdWN0aW9uCiAgICAgICAgICAgICMg0KDQsNC30LTQtdC70LXQvSAiLSIsICIsIiDQuNC70LggIi8iLCDQv9C+0YHQu9C1INGB0LTQtdC70LDRgtGMIHN0cmlwIC0tINC80L7Qs9GD0YIg0L7RgdGC0LDRgtGM0YHRjyDQv9GA0L7QsdC10LvRiwogICAgICAgICAgICBjb3VudHJ5X29mX3Byb2R1Y3Rpb24gPSBpbmZvLmdldCgnY291bnRyeU9mUHJvZHVjdGlvbicsIFtdKQogICAgICAgICAgICBpZiBjb3VudHJ5X29mX3Byb2R1Y3Rpb246CiAgICAgICAgICAgICAgICBpbXBvcnQgcmUKICAgICAgICAgICAgICAgIGNvdW50cnlfb2ZfcHJvZHVjdGlvbiA9IFt4LnN0cmlwKCkgZm9yIHggaW4gcmUuc3BsaXQoJ1stLC9dJywgY291bnRyeV9vZl9wcm9kdWN0aW9uKV0KICAgICAgICAgICAgICAgIGRlYnVnIGFuZCBwcmludCgn0KHRgtGA0LDQvdCwINC/0YDQvtC40LfQstC+0LTRgdGC0LLQsDonLCBjb3VudHJ5X29mX3Byb2R1Y3Rpb24pCgogICAgICAgICAgICBkZWJ1ZyBhbmQgcHJpbnQoKQoKICAgICAgICAgICAgIyBjb25uZWN0ID0gY3JlYXRlX2Nvbm5lY3QoKQogICAgICAgICAgICB0cnk6CiAgICAgICAgICAgICAgICAjINCh0L3QsNGH0LDQu9CwINC30LDQv9C+0LvQvdC10L3QuNC1INGC0LDQsdC70LjRhi3RgdC/0YDQsNCy0L7Rh9C90LjQutC+0LIKICAgICAgICAgICAgICAgIGlmIGFnZV9jYXRlZ29yeSBhbmQgYWdlX2NhdGVnb3J5LnN0cmlwKCk6CiAgICAgICAgICAgICAgICAgICAgYWdlX2NhdGVnb3J5ID0gYWdlX2NhdGVnb3J5LnN0cmlwKCkKCiAgICAgICAgICAgICAgICAgICAgY29ubmVjdC5leGVjdXRlKCdJTlNFUlQgT1IgSUdOT1JFIElOVE8gQWdlQ2F0ZWdvcnkgKG5hbWUpIFZBTFVFUyAoPyknLCAoYWdlX2NhdGVnb3J5LCkpCiAgICAgICAgICAgICAgICAgICAgKGFnZV9jYXRlZ29yeV9pZCwpID0gY29ubmVjdC5leGVjdXRlKCdTRUxFQ1QgaWQgRlJPTSBBZ2VDYXRlZ29yeSB3aGVyZSBuYW1lID0gPycsIChhZ2VfY2F0ZWdvcnksKSkuZmV0Y2hvbmUoKQogICAgICAgICAgICAgICAgICAgIGRlYnVnIGFuZCBwcmludCgnYWdlX2NhdGVnb3J5X2lkJywgYWdlX2NhdGVnb3J5X2lkKQoKICAgICAgICAgICAgICAgIGlmIGdlbnJlIGFuZCBnZW5yZS5zdHJpcCgpOgogICAgICAgICAgICAgICAgICAgIGdlbnJlID0gZ2VucmUuc3RyaXAoKQoKICAgICAgICAgICAgICAgICAgICBjb25uZWN0LmV4ZWN1dGUoJ0lOU0VSVCBPUiBJR05PUkUgSU5UTyBHZW5yZSAobmFtZSkgVkFMVUVTICg/KScsIChnZW5yZSwpKQogICAgICAgICAgICAgICAgICAgIChnZW5yZV9pZCwpID0gY29ubmVjdC5leGVjdXRlKCdTRUxFQ1QgaWQgRlJPTSBHZW5yZSB3aGVyZSBuYW1lID0gPycsIChnZW5yZSwpKS5mZXRjaG9uZSgpCiAgICAgICAgICAgICAgICAgICAgZGVidWcgYW5kIHByaW50KCdnZW5yZV9pZCcsIGdlbnJlX2lkKQoKICAgICAgICAgICAgICAgICMg0JTQvtCx0LDQstC70LXQvdC40LUg0YTQuNC70YzQvNCwINGBINGD0YfQtdGC0L7QvCBpZCDRgdC/0YDQsNCy0L7Rh9C90LjQutC+0LIKICAgICAgICAgICAgICAgIGNvbm5lY3QuZXhlY3V0ZSgnJycKICAgICAgICAgICAgICAgIElOU0VSVCBPUiBJR05PUkUgSU5UTyBNb3ZpZQogICAgICAgICAgICAgICAgKG5hbWUsIGZvcmVpZ25fbmFtZSwgZ2VucmVfaWQsIHllYXJfb2ZfcHJvZHVjdGlvbiwgbnVtYmVyX29mX3NlcmllcywgZHVyYXRpb24sIGNvbG9yLCBhZ2VfY2F0ZWdvcnlfaWQsCiAgICAgICAgICAgICAgICBhbm5vdGF0aW9uKSBWQUxVRVMgKD8sPyw/LD8sPyw/LD8sPyw/KScnJywKICAgICAgICAgICAgICAgIChuYW1lLCBmb3JlaWduX25hbWUsIGdlbnJlX2lkLCB5ZWFyX29mX3Byb2R1Y3Rpb24sIG51bWJlcl9vZl9zZXJpZXMsIGR1cmF0aW9uLCBjb2xvciwgYWdlX2NhdGVnb3J5X2lkLAogICAgICAgICAgICAgICAgIGFubm90YXRpb24pKQoKICAgICAgICAgICAgICAgIChtb3ZpZV9pZCwpID0gY29ubmVjdC5leGVjdXRlKCdTRUxFQ1QgaWQgRlJPTSBNb3ZpZSB3aGVyZSBuYW1lID0gPycsIChuYW1lLCkpLmZldGNob25lKCkKICAgICAgICAgICAgICAgIGRlYnVnIGFuZCBwcmludChtb3ZpZV9pZCkKCiAgICAgICAgICAgICAgICAjINCX0LDQv9C+0LvQvdC10L3QuNC1INGC0LDQsdC70LjRhiDRgdCy0Y/Qt9C10Lkg0YTQuNC70YzQvNCwINC4INC00YDRg9Cz0LjRhSDRgtCw0LHQu9C40YYKICAgICAgICAgICAgICAgIGZvciB4IGluIGRpcmVjdG9yOgogICAgICAgICAgICAgICAgICAgIHggPSB4LnN0cmlwKCkKICAgICAgICAgICAgICAgICAgICBpZiBub3QgeDoKICAgICAgICAgICAgICAgICAgICAgICAgY29udGludWUKCiAgICAgICAgICAgICAgICAgICAgIyDQlNC+0LHQsNCy0LvQtdC90LjQtSDRgNC10LbQuNGB0YHQtdGA0LAg0LIg0YLQsNCx0LvQuNGG0YMKICAgICAgICAgICAgICAgICAgICBjb25uZWN0LmV4ZWN1dGUoJ0lOU0VSVCBPUiBJR05PUkUgSU5UTyBEaXJlY3RvciAobmFtZSkgVkFMVUVTICg/KScsICh4LCkpCiAgICAgICAgICAgICAgICAgICAgKGRpcmVjdG9yX2lkLCkgPSBjb25uZWN0LmV4ZWN1dGUoJ1NFTEVDVCBpZCBGUk9NIERpcmVjdG9yIHdoZXJlIG5hbWUgPSA/JywgKHgsKSkuZmV0Y2hvbmUoKQogICAgICAgICAgICAgICAgICAgIGRlYnVnIGFuZCBwcmludCgnZGlyZWN0b3JfaWQnLCBkaXJlY3Rvcl9pZCkKCiAgICAgICAgICAgICAgICAgICAgIyDQodC+0LfQtNCw0L3QuNC1INGB0LLRj9C30LgKICAgICAgICAgICAgICAgICAgICBjb25uZWN0LmV4ZWN1dGUoJ0lOU0VSVCBPUiBJR05PUkUgSU5UTyBMaW5rX01vdmllX0RpcmVjdG9yIChtb3ZpZV9pZCwgZGlyZWN0b3JfaWQpIFZBTFVFUyAoPyw/KScsIChtb3ZpZV9pZCwgZGlyZWN0b3JfaWQpKQoKICAgICAgICAgICAgICAgIGZvciB4IGluIHN0dWRpbzoKICAgICAgICAgICAgICAgICAgICB4ID0geC5zdHJpcCgpCiAgICAgICAgICAgICAgICAgICAgaWYgbm90IHg6CiAgICAgICAgICAgICAgICAgICAgICAgIGNvbnRpbnVlCgogICAgICAgICAgICAgICAgICAgICMg0JTQvtCx0LDQstC70LXQvdC40LUg0YHRgtGD0LTQuNC4INCyINGC0LDQsdC70LjRhtGDCiAgICAgICAgICAgICAgICAgICAgY29ubmVjdC5leGVjdXRlKCdJTlNFUlQgT1IgSUdOT1JFIElOVE8gU3R1ZGlvIChuYW1lKSBWQUxVRVMgKD8pJywgKHgsKSkKICAgICAgICAgICAgICAgICAgICAoc3R1ZGlvX2lkLCkgPSBjb25uZWN0LmV4ZWN1dGUoJ1NFTEVDVCBpZCBGUk9NIFN0dWRpbyB3aGVyZSBuYW1lID0gPycsICh4LCkpLmZldGNob25lKCkKICAgICAgICAgICAgICAgICAgICBkZWJ1ZyBhbmQgcHJpbnQoJ3N0dWRpb19pZCcsIHN0dWRpb19pZCkKCiAgICAgICAgICAgICAgICAgICAgIyDQodC+0LfQtNCw0L3QuNC1INGB0LLRj9C30LgKICAgICAgICAgICAgICAgICAgICBjb25uZWN0LmV4ZWN1dGUoJ0lOU0VSVCBPUiBJR05PUkUgSU5UTyBMaW5rX01vdmllX1N0dWRpbyAobW92aWVfaWQsIHN0dWRpb19pZCkgVkFMVUVTICg/LD8pJywgKG1vdmllX2lkLCBzdHVkaW9faWQpKQoKICAgICAgICAgICAgICAgIGZvciB4IGluIGNvdW50cnlfb2ZfcHJvZHVjdGlvbjoKICAgICAgICAgICAgICAgICAgICB4ID0geC5zdHJpcCgpCiAgICAgICAgICAgICAgICAgICAgaWYgbm90IHg6CiAgICAgICAgICAgICAgICAgICAgICAgIGNvbnRpbnVlCgogICAgICAgICAgICAgICAgICAgICMg0JTQvtCx0LDQstC70LXQvdC40LUg0YHRgtGD0LTQuNC4INCyINGC0LDQsdC70LjRhtGDCiAgICAgICAgICAgICAgICAgICAgY29ubmVjdC5leGVjdXRlKCdJTlNFUlQgT1IgSUdOT1JFIElOVE8gQ291bnRyeU9mUHJvZHVjdGlvbiAobmFtZSkgVkFMVUVTICg/KScsICh4LCkpCiAgICAgICAgICAgICAgICAgICAgKGNvdW50cnlfb2ZfcHJvZHVjdGlvbl9pZCwpID0gY29ubmVjdC5leGVjdXRlKCdTRUxFQ1QgaWQgRlJPTSBDb3VudHJ5T2ZQcm9kdWN0aW9uIHdoZXJlIG5hbWUgPSA/JywgKHgsKSkuZmV0Y2hvbmUoKQogICAgICAgICAgICAgICAgICAgIGRlYnVnIGFuZCBwcmludCgnY291bnRyeV9vZl9wcm9kdWN0aW9uX2lkJywgY291bnRyeV9vZl9wcm9kdWN0aW9uX2lkKQoKICAgICAgICAgICAgICAgICAgICAjINCh0L7Qt9C00LDQvdC40LUg0YHQstGP0LfQuAogICAgICAgICAgICAgICAgICAgIGNvbm5lY3QuZXhlY3V0ZSgnSU5TRVJUIE9SIElHTk9SRSBJTlRPIExpbmtfTW92aWVfQ291bnRyeU9mUHJvZHVjdGlvbiAobW92aWVfaWQsIGNvdW50cnlfb2ZfcHJvZHVjdGlvbl9pZCkgVkFMVUVTICg/LD8pJywgKG1vdmllX2lkLCBjb3VudHJ5X29mX3Byb2R1Y3Rpb25faWQpKQoKICAgICAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyBlOgogICAgICAgICAgICAgICAgcHJpbnQoJ3NxbDonLCBlLCAnLCB3aGVuOicsIGZpbG0pCgogICAgICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZToKICAgICAgICAgICAgcHJpbnQoJ3dhcm46JywgZSwgJywgd2hlbjonLCBmaWxtKQoKICAgIGNvbm5lY3QuY29tbWl0KCkKICAgIGNvbm5lY3QuY2xvc2UoKQoK'
open('get_script.py', 'wb').write(base64.b64decode(text))

sql_text = b'LS0tLSBOT1RFOiDQo9C00LDQu9C40YLRjCwg0LjRgdC/0L7Qu9GM0LfRg9C10YLRgdGPINC00LvRjyDRgtC10YHRgtC40YDQvtCy0LDQvdC40Y8g0LfQsNC/0L7Qu9C90LXQvdC40Y8g0LHQtA0KLS1kcm9wIHRhYmxlIElGIEVYSVNUUyBNb3ZpZTsNCi0tZHJvcCB0YWJsZSBJRiBFWElTVFMgRGlyZWN0b3I7DQotLWRyb3AgdGFibGUgSUYgRVhJU1RTIEdlbnJlOw0KLS1kcm9wIHRhYmxlIElGIEVYSVNUUyBTdHVkaW87DQotLWRyb3AgdGFibGUgSUYgRVhJU1RTIEFnZUNhdGVnb3J5Ow0KLS1kcm9wIHRhYmxlIElGIEVYSVNUUyBDb3VudHJ5T2ZQcm9kdWN0aW9uOw0KLS0NCi0tZHJvcCB0YWJsZSBJRiBFWElTVFMgTGlua19Nb3ZpZV9EaXJlY3RvcjsNCi0tZHJvcCB0YWJsZSBJRiBFWElTVFMgTGlua19Nb3ZpZV9TdHVkaW87DQotLWRyb3AgdGFibGUgSUYgRVhJU1RTIExpbmtfTW92aWVfQ291bnRyeU9mUHJvZHVjdGlvbjsNCg0KDQpDUkVBVEUgVEFCTEUgSUYgTk9UIEVYSVNUUyBNb3ZpZSAoDQogICAgaWQgSU5URUdFUiBQUklNQVJZIEtFWSwNCg0KICAgIC0tINCd0LDQt9Cy0LDQvdC40LUNCiAgICBuYW1lIFRFWFQgTk9UIE5VTEwsDQoNCiAgICAtLSDQndCw0LjQvNC10L3QvtCy0LDQvdC40LUg0L3QsCDQuNC90L7RgdGC0YDQsNC90L3QvtC8INGP0LfRi9C60LUNCiAgICBmb3JlaWduX25hbWUgVEVYVCwNCg0KICAgIC0tINCW0LDQvdGADQogICAgZ2VucmVfaWQgSU5URUdFUiwNCg0KICAgIC0tINCT0L7QtCDQv9GA0L7QuNC30LLQvtC00YHRgtCy0LANCiAgICB5ZWFyX29mX3Byb2R1Y3Rpb24gSU5URUdFUiwNCg0KICAgIC0tINCa0L7Qu9C40YfQtdGB0YLQstC+INGB0LXRgNC40LkNCiAgICBudW1iZXJfb2Zfc2VyaWVzIElOVEVHRVIsDQoNCiAgICAtLSDQn9GA0L7QtNC+0LvQttC40YLQtdC70YzQvdC+0YHRgtGMINC/0L7QutCw0LfQsCAo0LzQuNC90YPRgtGLKQ0KICAgIGR1cmF0aW9uIElOVEVHRVIsDQoNCiAgICAtLSDQptCy0LXRgjogVHJ1ZSAtLSDRhtCy0LXRgtC90L7QuSwgRmFsc2UgLS0g0YfQtdGA0L3Qvi3QsdC10LvRi9C5DQogICAgY29sb3IgQk9PTEVBTiwNCg0KICAgIC0tINCS0L7Qt9GA0LDRgdGC0L3QsNGPINC60LDRgtC10LPQvtGA0LjRjyDQt9GA0LjRgtC10LvRjNGB0LrQvtC5INCw0YPQtNC40YLQvtGA0LjQuA0KICAgIGFnZV9jYXRlZ29yeV9pZCBJTlRFR0VSLA0KDQogICAgLS0g0JDQvdC90L7RgtCw0YbQuNGPDQogICAgYW5ub3RhdGlvbiBURVhULA0KDQogICAgQ09OU1RSQUlOVCBuYW1lX3VuaXF1ZSBVTklRVUUgKG5hbWUpDQopOw0KDQoNCi0tINCg0LXQttC40YHRgdC10YANCkNSRUFURSBUQUJMRSBJRiBOT1QgRVhJU1RTIERpcmVjdG9yICgNCiAgICBpZCBJTlRFR0VSIFBSSU1BUlkgS0VZLA0KICAgIG5hbWUgVEVYVCBOT1QgTlVMTCwNCg0KICAgIENPTlNUUkFJTlQgbmFtZV91bmlxdWUgVU5JUVVFIChuYW1lKQ0KKTsNCg0KQ1JFQVRFIFRBQkxFIElGIE5PVCBFWElTVFMgR2VucmUgKA0KICAgIGlkIElOVEVHRVIgUFJJTUFSWSBLRVksDQogICAgbmFtZSBURVhUIE5PVCBOVUxMLA0KDQogICAgQ09OU1RSQUlOVCBuYW1lX3VuaXF1ZSBVTklRVUUgKG5hbWUpDQopOw0KDQotLSDQodGC0YPQtNC40Y8t0L/RgNC+0LjQt9Cy0L7QtNC40YLQtdC70YwNCkNSRUFURSBUQUJMRSBJRiBOT1QgRVhJU1RTIFN0dWRpbyAoDQogICAgaWQgSU5URUdFUiBQUklNQVJZIEtFWSwNCiAgICBuYW1lIFRFWFQgTk9UIE5VTEwsDQoNCiAgICBDT05TVFJBSU5UIG5hbWVfdW5pcXVlIFVOSVFVRSAobmFtZSkNCik7DQoNCkNSRUFURSBUQUJMRSBJRiBOT1QgRVhJU1RTIEFnZUNhdGVnb3J5ICgNCiAgICBpZCBJTlRFR0VSIFBSSU1BUlkgS0VZLA0KICAgIG5hbWUgVEVYVCBOT1QgTlVMTCwNCg0KICAgIENPTlNUUkFJTlQgbmFtZV91bmlxdWUgVU5JUVVFIChuYW1lKQ0KKTsNCg0KLS0g0KHRgtGA0LDQvdCwINC/0YDQvtC40LfQstC+0LTRgdGC0LLQsA0KQ1JFQVRFIFRBQkxFIElGIE5PVCBFWElTVFMgQ291bnRyeU9mUHJvZHVjdGlvbiAoDQogICAgaWQgSU5URUdFUiBQUklNQVJZIEtFWSwNCiAgICBuYW1lIFRFWFQgTk9UIE5VTEwsDQoNCiAgICBDT05TVFJBSU5UIG5hbWVfdW5pcXVlIFVOSVFVRSAobmFtZSkNCik7DQoNCg0KQ1JFQVRFIFRBQkxFIElGIE5PVCBFWElTVFMgTGlua19Nb3ZpZV9EaXJlY3RvciAoDQogICAgbW92aWVfaWQgSU5URUdFUiwNCiAgICBkaXJlY3Rvcl9pZCBJTlRFR0VSLA0KDQogICAgUFJJTUFSWSBLRVkgKG1vdmllX2lkLCBkaXJlY3Rvcl9pZCkNCik7DQoNCkNSRUFURSBUQUJMRSBJRiBOT1QgRVhJU1RTIExpbmtfTW92aWVfU3R1ZGlvICgNCiAgICBtb3ZpZV9pZCBJTlRFR0VSLA0KICAgIHN0dWRpb19pZCBJTlRFR0VSLA0KDQogICAgUFJJTUFSWSBLRVkgKG1vdmllX2lkLCBzdHVkaW9faWQpDQopOw0KDQpDUkVBVEUgVEFCTEUgSUYgTk9UIEVYSVNUUyBMaW5rX01vdmllX0NvdW50cnlPZlByb2R1Y3Rpb24gKA0KICAgIG1vdmllX2lkIElOVEVHRVIsDQogICAgY291bnRyeV9vZl9wcm9kdWN0aW9uX2lkIElOVEVHRVIsDQoNCiAgICBQUklNQVJZIEtFWSAobW92aWVfaWQsIGNvdW50cnlfb2ZfcHJvZHVjdGlvbl9pZCkNCik7DQo='
open('init_db_opendata_register_movie.sql', 'wb').write(base64.b64decode(sql_text))
