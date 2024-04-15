#version 120
#define FXAA_SPAN_MAX 8.0
#define FXAA_REDUCE_MUL 1.0/8.0
#define FXAA_REDUCE_MIN 1.0/128.0

const float COLOR_FACTOR = 18.0;
const float DITHER_STRENGTH = 0.015; // Reduced dither strength
const float PIXELATE_STRENGTH = 1.0; // Increased pixelation strength
const float SCANLINE_STRENGTH = 0.01; // Slightly reduced scanline strength
const float COLOR_SHIFT_INTENSITY = 0.52; // Reduced color shift intensity
const float BLEEDING_STRENGTH = 0.005; // Adjust the strength of color bleeding
const float VIGNETTE_STRENGTH = 0.2; // Adjust the strength of vignette effect

const mat4 DITH = mat4(
    -8.0, 0.0, -6.0, 2.0,
    4.0, -4.0, 6.0, -2.0,
    -6.0, 2.0, -8.0, 0.0,
    6.0, -2.0, 4.0, -4.0
);

uniform sampler2D texSampler;
uniform float screenSizeX;
uniform float screenSizeY;

// Function to calculate pixelation
vec3 pixelate(vec2 uv, vec2 texel) {
    vec2 q = texel * PIXELATE_STRENGTH;
    uv = floor(uv / q) * q;
    return texture2D(texSampler, uv).rgb;
}

void main( void ) {
    vec2 uv = gl_TexCoord[0].st;

    vec2 texel = vec2(
        1.0 / screenSizeX,
        1.0 / screenSizeY
    );

    // Apply pixelation effect
    vec3 pixelatedColor = pixelate(uv, texel);

    // Apply stronger dithering
    vec2 ruv = uv * (1.0 / texel);
    ruv = floor(ruv + 0.001);

    pixelatedColor += DITH[int(mod(ruv.x, 4.0))][int(mod(ruv.y, 4.0))] * DITHER_STRENGTH;
    pixelatedColor = floor(pixelatedColor * COLOR_FACTOR) / COLOR_FACTOR;

    // CRT effect - Scanlines
    float scanline = sin(gl_FragCoord.y * 200.0) * SCANLINE_STRENGTH;
    pixelatedColor -= vec3(scanline);

    // CRT effect - Color shift
    pixelatedColor *= vec3(0.98, 1.02, 0.98); // Adjust color distortion

    // CRT effect - Color bleeding
    vec3 neighborColor = texture2D(texSampler, uv + vec2(0.005, 0.0)).rgb; // Sample color from a neighboring pixel
    pixelatedColor += (neighborColor - pixelatedColor) * BLEEDING_STRENGTH;

    // Vignette effect
    float vignette = smoothstep(1.0, VIGNETTE_STRENGTH, length(uv - 0.5));
    pixelatedColor *= vignette;

    // Output the final color
    gl_FragColor = vec4(pixelatedColor, 1.0);
}
