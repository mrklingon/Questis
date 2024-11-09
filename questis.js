function divide () {
    if (2 <= stack.length) {
        v1 = stack.pop()
        v2 = stack.pop()
    }
    if (v2 != 0) {
        Z = Math.round(v1 / v2)
        stack.push(Z)
        dispBinary(Z, 0)
        pause(1000)
        light.setAll(0x000000)
        Z = 0
    }
}
function subtract () {
    if (2 <= stack.length) {
        v1 = stack.pop()
        v2 = stack.pop()
        Z = v1 - v2
        stack.push(Z)
        dispBinary(Z, 0)
        pause(1000)
        light.setAll(0x000000)
        Z = 0
    }
}
function zing () {
    light.showAnimation(light.rainbowAnimation, 500)
    for (let index = 0; index <= Math.randomRange(5, 10); index++) {
        dispBinary(Math.randomRange(0, 1023), 0)
        pause(1000)
    }
    light.setAll(0x000000)
    Z = 0
    action = 0
    stack = []
}
function dispBinary (Value: number, Position: number) {
    light.setAll(0x000000)
    if (Value < 0) {
        P = Colors.Red
    } else {
        P = Colors.Green
    }
    Scratch = Math.abs(Value)
    Start = 0
    if (Scratch != 0) {
        while (Scratch > 0) {
            if (1 == Scratch % 2) {
                light.setPixelColor(Start + Position, P)
            } else {
                light.setPixelColor(Start + Position, light.rgb(0, 0, 51))
            }
            Start += 1
            Scratch = Math.trunc(Scratch / 2)
        }
    } else {
        light.setPixelColor(Position, light.rgb(0, 0, 51))
    }
}
input.onGesture(Gesture.Shake, function () {
    zing()
})
input.buttonsAB.onEvent(ButtonEvent.Click, function () {
    if (!(input.switchRight())) {
        stack.push(Z)
        Z = 0
        light.setAll(0x000000)
    } else {
        if (0 < stack.length) {
            Z = stack.pop()
            dispBinary(Z, 0)
            pause(1000)
            light.setAll(0x000000)
            Z = 0
        }
    }
})
input.buttonB.onEvent(ButtonEvent.Click, function () {
    if (!(input.switchRight())) {
        Z += -1
        dispBinary(Z, 0)
    } else {
        if (action == 1) {
            mult()
        }
        if (action == 2) {
            divide()
        }
        if (action == 3) {
            add()
        }
        if (action == 4) {
            subtract()
        }
    }
})
function mult () {
    if (2 <= stack.length) {
        v1 = stack.pop()
        v2 = stack.pop()
        Z = v1 * v2
        stack.push(Z)
        dispBinary(Z, 0)
        pause(1000)
        light.setAll(0x000000)
        Z = 0
    }
}
function add () {
    if (2 <= stack.length) {
        v1 = stack.pop()
        v2 = stack.pop()
        Z = v1 + v2
        stack.push(Z)
        dispBinary(Z, 0)
        pause(1000)
    }
    light.setAll(0x000000)
    Z = 0
}
input.pinA1.onEvent(ButtonEvent.Click, function () {
    dispBinary(stack.length, 0)
    pause(1000)
    light.setAll(0x000000)
})
input.onSwitchMoved(SwitchDirection.Left, function () {
    light.setAll(0x000000)
})
input.onSwitchMoved(SwitchDirection.Right, function () {
    light.setAll(0x000000)
})
input.buttonA.onEvent(ButtonEvent.Click, function () {
    if (!(input.switchRight())) {
        Z += 1
        dispBinary(Z, 0)
    } else {
        action += 1
        action = action % 5
        dispBinary(action, 6)
    }
})
input.pinA2.onEvent(ButtonEvent.Click, function () {
    dispBinary(stack.length, 0)
    for (let value of stack) {
        dispBinary(value, 0)
        pause(500)
    }
    light.setAll(0x000000)
})
let Start = 0
let Scratch = 0
let P = 0
let action = 0
let Z = 0
let v2 = 0
let v1 = 0
let stack: number[] = []
zing()
