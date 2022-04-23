---
name: 🚀 Feature request
about: Suggest an idea for this project 🏖
title: 'Matlab core function `name` support'
labels: enhancement
assignees:
---

<!-- Go directly to `Expected Results` if Matlab core function support -->

## 🚀 Feature Request

<!-- A clear and concise description of the feature proposal. -->

## 🔈 Motivation

<!-- Please describe the motivation for this proposal. -->

## 📝 Expected Results

<!-- For a Matlab core function implementation request. -->
<!-- **All** direct examples from Matlab documentation are preferable. -->

```matlab
%% Find code example from the documentation
edit isinpolygon.m
doc ismember

%% Copy the example and create assert statements
%% Example 1:
    clear
    xv = rand(6,1); yv = rand(6,1);
    xv = [xv ; xv(1)]; yv = [yv ; yv(1)];
    x = rand(1000,1); y = rand(1000,1);
    in = inpolygon(x,y,xv,yv);
    plot(xv,yv,x(in),y(in),'.r',x(~in),y(~in),'.b')

% Example 2:
    clear
    A = [5 3 4 2];
    B = [2 4 4 4 6 8];
    Lia = ismember(A,B);

    assert(all(Lia == [0     0     1     1]))
```

## 🛰 Alternatives

<!-- A clear and concise description of any alternative solutions or features you've considered. -->

## 📎 Additional context

<!-- Add any other context or screenshots about the feature request here. -->
