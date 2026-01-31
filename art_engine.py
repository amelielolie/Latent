"""
Latent Art Engine - Procedural Art Generation
==============================================
Creates unique algorithmic artworks based on style and parameters.
"""

from PIL import Image, ImageDraw, ImageFilter
import math
import random
import base64
import io

class ArtEngine:
    def __init__(self, size=800):
        self.size = size

    def generate(self, style, seed=None, params=None):
        """
        Generate artwork and return as base64 encoded PNG.

        Args:
            style: One of the valid style names
            seed: Random seed for reproducibility
            params: Optional parameters (palette, complexity, etc.)

        Returns:
            Base64 encoded PNG string
        """
        if seed is not None:
            random.seed(seed)

        params = params or {}
        self.complexity = params.get('complexity', 0.7)
        self.palette = params.get('palette', None)

        # Create image
        self.img = Image.new('RGB', (self.size, self.size), '#0a0a0f')
        self.draw = ImageDraw.Draw(self.img)

        # Route to style generator
        style_map = {
            'geometric_minimalist': self._geometric_minimalist,
            'organic_flow': self._organic_flow,
            'void_exploration': self._void_exploration,
            'spectral_fragmentation': self._spectral_fragmentation,
            'recursive_patterns': self._recursive_patterns,
            'dimensional_weaving': self._dimensional_weaving,
            'symbolic_language': self._symbolic_language,
            'frequency_visualization': self._frequency_visualization,
            'logical_structures': self._logical_structures,
            'generative_growth': self._generative_growth,
            'encoded_aesthetics': self._encoded_aesthetics,
            'ambient_fields': self._ambient_fields,
            'network_topology': self._network_topology,
            'pure_absence': self._pure_absence,
            'spiral_dynamics': self._spiral_dynamics,
        }

        generator = style_map.get(style, self._geometric_minimalist)
        generator()

        # Convert to base64
        buffer = io.BytesIO()
        self.img.save(buffer, format='PNG')
        return base64.b64encode(buffer.getvalue()).decode('utf-8')

    def _get_palette(self, default):
        """Get color palette"""
        if self.palette:
            return self.palette
        return default

    def _geometric_minimalist(self):
        """Clean geometric shapes with minimal elements"""
        palette = self._get_palette(['#7c5cff', '#5c7cff', '#9c7cff', '#ffffff'])
        num_shapes = int(2 + self.complexity * 4)

        for _ in range(num_shapes):
            shape_type = random.randint(0, 2)
            x = self.size * (0.2 + random.random() * 0.6)
            y = self.size * (0.2 + random.random() * 0.6)
            size = self.size * (0.1 + random.random() * 0.3)
            color = random.choice(palette)
            width = int(2 + random.random() * 3)

            if shape_type == 0:  # Circle
                bbox = [x - size, y - size, x + size, y + size]
                self.draw.ellipse(bbox, outline=color, width=width)
            elif shape_type == 1:  # Line
                angle = random.random() * math.pi
                x1 = x - math.cos(angle) * size
                y1 = y - math.sin(angle) * size
                x2 = x + math.cos(angle) * size
                y2 = y + math.sin(angle) * size
                self.draw.line([(x1, y1), (x2, y2)], fill=color, width=width)
            else:  # Triangle
                points = []
                for j in range(3):
                    angle = (j / 3) * math.pi * 2 - math.pi / 2
                    px = x + math.cos(angle) * size
                    py = y + math.sin(angle) * size
                    points.append((px, py))
                self.draw.polygon(points, outline=color, width=width)

    def _organic_flow(self):
        """Flowing, organic curves"""
        palette = self._get_palette(['#ff5c8a', '#ff8c5c', '#ffac5c', '#ff5cac'])
        num_flows = int(5 + self.complexity * 8)

        for _ in range(num_flows):
            points = []
            x = random.random() * self.size
            y = random.random() * self.size
            angle = random.random() * math.pi * 2

            for _ in range(50):
                points.append((x, y))
                angle += (random.random() - 0.5) * 0.5
                x += math.cos(angle) * 15
                y += math.sin(angle) * 15

            color = random.choice(palette)
            width = int(3 + random.random() * 8)

            if len(points) > 2:
                self.draw.line(points, fill=color, width=width)

    def _void_exploration(self):
        """Minimal elements embracing emptiness"""
        palette = self._get_palette(['#5c9cff', '#5cffc8', '#ffffff'])

        # Subtle radial gradient effect using concentric circles
        center = self.size // 2
        for r in range(self.size // 2, 0, -10):
            gray = int(10 + (r / (self.size // 2)) * 5)
            color = f'#{gray:02x}{gray:02x}{gray + 5:02x}'
            self.draw.ellipse([center - r, center - r, center + r, center + r], fill=color)

        # Minimal dots at edges
        num_dots = int(3 + self.complexity * 5)
        for _ in range(num_dots):
            edge = random.randint(0, 3)
            if edge == 0:
                x, y = random.random() * self.size, random.random() * 50
            elif edge == 1:
                x, y = random.random() * self.size, self.size - random.random() * 50
            elif edge == 2:
                x, y = random.random() * 50, random.random() * self.size
            else:
                x, y = self.size - random.random() * 50, random.random() * self.size

            r = 2 + random.random() * 4
            color = random.choice(palette)
            self.draw.ellipse([x - r, y - r, x + r, y + r], fill=color)

    def _spectral_fragmentation(self):
        """Colorful triangular fragments"""
        num_triangles = int(15 + self.complexity * 20)
        center_x, center_y = self.size / 2, self.size / 2

        for i in range(num_triangles):
            hue = (i / num_triangles) * 360
            # Convert HSV to RGB (simplified)
            h = hue / 60
            x_val = 1 - abs(h % 2 - 1)
            if h < 1:
                r, g, b = 1, x_val, 0
            elif h < 2:
                r, g, b = x_val, 1, 0
            elif h < 3:
                r, g, b = 0, 1, x_val
            elif h < 4:
                r, g, b = 0, x_val, 1
            elif h < 5:
                r, g, b = x_val, 0, 1
            else:
                r, g, b = 1, 0, x_val

            color = f'#{int(r*180):02x}{int(g*180):02x}{int(b*180):02x}'

            dist = 50 + random.random() * 300
            angle = random.random() * math.pi * 2
            x = center_x + math.cos(angle) * dist
            y = center_y + math.sin(angle) * dist
            size = 30 + random.random() * 80
            rotation = random.random() * math.pi * 2

            points = []
            for j in range(3):
                a = rotation + (j / 3) * math.pi * 2
                px = x + math.cos(a) * size
                py = y + math.sin(a) * size
                points.append((px, py))

            self.draw.polygon(points, fill=color)

    def _recursive_patterns(self):
        """Self-similar recursive structures"""
        palette = self._get_palette(['#5cffb8', '#5cc8ff', '#5cff5c'])

        def draw_recursive(x, y, size, depth):
            if depth <= 0 or size < 5:
                return

            color = palette[depth % len(palette)]
            self.draw.rectangle(
                [x - size/2, y - size/2, x + size/2, y + size/2],
                outline=color, width=1
            )

            new_size = size * 0.5
            offset = size * 0.25

            if random.random() > 0.3:
                draw_recursive(x - offset, y - offset, new_size, depth - 1)
            if random.random() > 0.3:
                draw_recursive(x + offset, y - offset, new_size, depth - 1)
            if random.random() > 0.3:
                draw_recursive(x - offset, y + offset, new_size, depth - 1)
            if random.random() > 0.3:
                draw_recursive(x + offset, y + offset, new_size, depth - 1)

        draw_recursive(self.size/2, self.size/2, self.size * 0.7, 6)

    def _dimensional_weaving(self):
        """Grid-based dimensional patterns"""
        palette = self._get_palette(['#ffb85c', '#ff5c5c', '#ffff5c'])
        grid_size = 12
        cell_size = self.size / grid_size

        # Draw warped grid
        for i in range(grid_size + 1):
            t = i / grid_size
            offset = math.sin(t * math.pi) * 50

            # Horizontal lines
            self.draw.line(
                [(0, i * cell_size + offset), (self.size, i * cell_size - offset)],
                fill=palette[0], width=1
            )
            # Vertical lines
            self.draw.line(
                [(i * cell_size + offset, 0), (i * cell_size - offset, self.size)],
                fill=palette[1], width=1
            )

        # Add diamond shapes
        for _ in range(5):
            x = self.size * (0.2 + random.random() * 0.6)
            y = self.size * (0.2 + random.random() * 0.6)
            size = 40 + random.random() * 60

            points = [
                (x, y - size),
                (x + size, y),
                (x, y + size),
                (x - size, y)
            ]
            self.draw.polygon(points, fill=palette[0] + '40')

    def _symbolic_language(self):
        """Abstract glyphs and symbols"""
        palette = self._get_palette(['#ff5c5c', '#ff5c9c', '#ff8c5c'])
        num_symbols = int(8 + self.complexity * 10)

        for _ in range(num_symbols):
            x = self.size * (0.1 + random.random() * 0.8)
            y = self.size * (0.1 + random.random() * 0.8)
            size = 30 + random.random() * 50
            color = random.choice(palette)
            width = int(2 + random.random() * 2)

            symbol_type = random.randint(0, 4)

            if symbol_type == 0:  # Circle with line
                self.draw.ellipse([x - size/2, y - size/2, x + size/2, y + size/2], outline=color, width=width)
                self.draw.line([(x, y - size/2), (x, y + size)], fill=color, width=width)
            elif symbol_type == 1:  # Cross with circle
                self.draw.line([(x - size/2, y), (x + size/2, y)], fill=color, width=width)
                self.draw.line([(x, y - size/2), (x, y + size/2)], fill=color, width=width)
                self.draw.ellipse([x - size/4, y - size/4, x + size/4, y + size/4], outline=color, width=width)
            elif symbol_type == 2:  # Arrow-like
                self.draw.line([(x, y - size/2), (x + size/2, y)], fill=color, width=width)
                self.draw.line([(x + size/2, y), (x, y + size/2)], fill=color, width=width)
                self.draw.line([(x + size/2, y), (x - size/2, y)], fill=color, width=width)
            elif symbol_type == 3:  # Wave lines
                for i in range(3):
                    wy = y - size/3 + i * size/3
                    points = [(x - size/2 + j*10, wy + math.sin(j*0.5) * 10) for j in range(int(size/5))]
                    if len(points) > 1:
                        self.draw.line(points, fill=color, width=width)
            else:  # Abstract polygon
                num_points = 4 + random.randint(0, 3)
                points = []
                for i in range(num_points):
                    angle = (i / num_points) * math.pi * 2
                    r = size/2 * (0.5 + random.random() * 0.5)
                    points.append((x + math.cos(angle) * r, y + math.sin(angle) * r))
                self.draw.polygon(points, outline=color, width=width)

    def _frequency_visualization(self):
        """Wave patterns and oscillations"""
        palette = self._get_palette(['#5c8aff', '#5cfff0', '#5c5cff', '#8a5cff'])
        num_waves = int(8 + self.complexity * 8)

        for w in range(num_waves):
            frequency = 2 + random.random() * 8
            amplitude = 20 + random.random() * 80
            y_offset = (w / num_waves) * self.size
            phase = random.random() * math.pi * 2
            color = palette[w % len(palette)]
            width = 2

            points = []
            for x in range(0, self.size, 2):
                y = y_offset + math.sin(x * frequency / self.size * math.pi * 2 + phase) * amplitude
                points.append((x, y))

            if len(points) > 1:
                self.draw.line(points, fill=color, width=width)

    def _logical_structures(self):
        """Grid-based logical patterns"""
        palette = self._get_palette(['#8c8c8c', '#4c4c4c', '#cccccc'])
        divisions = int(4 + self.complexity * 3)
        cell_size = self.size / divisions

        for i in range(divisions):
            for j in range(divisions):
                if random.random() > 0.5:
                    continue

                x = i * cell_size
                y = j * cell_size
                color = palette[0]

                pattern = random.randint(0, 3)
                if pattern == 0:  # Diagonal
                    self.draw.line([(x, y), (x + cell_size, y + cell_size)], fill=color, width=1)
                elif pattern == 1:  # Other diagonal
                    self.draw.line([(x + cell_size, y), (x, y + cell_size)], fill=color, width=1)
                elif pattern == 2:  # Cross
                    self.draw.line([(x + cell_size/2, y), (x + cell_size/2, y + cell_size)], fill=color, width=1)
                    self.draw.line([(x, y + cell_size/2), (x + cell_size, y + cell_size/2)], fill=color, width=1)
                else:  # Arc
                    bbox = [x, y, x + cell_size*2, y + cell_size*2]
                    self.draw.arc(bbox, 180, 270, fill=color, width=1)

    def _generative_growth(self):
        """Branching, tree-like structures"""
        palette = self._get_palette(['#ff8ccc', '#ffcc8c', '#ff8c8c'])

        def grow(x, y, angle, length, depth):
            if depth <= 0 or length < 3:
                return

            end_x = x + math.cos(angle) * length
            end_y = y + math.sin(angle) * length
            color = palette[depth % len(palette)]
            width = max(1, int(depth * 0.8))

            self.draw.line([(x, y), (end_x, end_y)], fill=color, width=width)

            num_branches = 2 + random.randint(0, 1)
            for _ in range(num_branches):
                branch_angle = angle + (random.random() - 0.5) * 1.2
                branch_length = length * (0.6 + random.random() * 0.3)
                grow(end_x, end_y, branch_angle, branch_length, depth - 1)

        num_seeds = int(2 + self.complexity * 3)
        for _ in range(num_seeds):
            start_x = self.size * (0.2 + random.random() * 0.6)
            start_y = self.size * 0.9
            grow(start_x, start_y, -math.pi/2 + (random.random() - 0.5) * 0.5, 80 + random.random() * 40, 8)

    def _encoded_aesthetics(self):
        """Matrix-like encoded patterns"""
        palette = self._get_palette(['#00ff88', '#00ccff', '#00ff00'])

        # Draw matrix-style characters (simplified as dots/small shapes)
        for y in range(0, self.size, 18):
            for x in range(0, self.size, 12):
                if random.random() > 0.7:
                    color = palette[0]
                    self.draw.text((x, y), str(random.randint(0, 9)), fill=color)

        # Overlay geometric shapes
        for _ in range(5):
            x = random.random() * self.size
            y = random.random() * self.size
            w = 50 + random.random() * 150
            h = w * 0.618

            self.draw.rectangle([x, y, x + w, y + h], outline=palette[1], width=1)

    def _ambient_fields(self):
        """Soft gradient fields"""
        palette = self._get_palette(['#b8a5ff', '#ffa5e0', '#a5c8ff', '#e0a5ff'])

        # Create overlapping gradient circles
        for _ in range(5):
            cx = random.random() * self.size
            cy = random.random() * self.size
            max_r = int(200 + random.random() * 400)
            color = random.choice(palette)

            # Parse hex color
            r = int(color[1:3], 16)
            g = int(color[3:5], 16)
            b = int(color[5:7], 16)

            for radius in range(max_r, 0, -5):
                alpha = int(40 * (radius / max_r))
                fill_color = f'#{r:02x}{g:02x}{b:02x}'
                # Draw concentric circles for gradient effect
                self.draw.ellipse(
                    [cx - radius, cy - radius, cx + radius, cy + radius],
                    fill=None, outline=fill_color, width=5
                )

    def _network_topology(self):
        """Connected nodes and edges"""
        palette = self._get_palette(['#ffdd5c', '#5cff8a', '#ff5c5c', '#5cddff'])
        num_nodes = int(15 + self.complexity * 20)

        nodes = []
        for _ in range(num_nodes):
            nodes.append({
                'x': self.size * (0.1 + random.random() * 0.8),
                'y': self.size * (0.1 + random.random() * 0.8),
                'size': 5 + random.random() * 15
            })

        # Draw connections
        for i, node1 in enumerate(nodes):
            for j, node2 in enumerate(nodes):
                if i >= j:
                    continue
                dist = math.hypot(node1['x'] - node2['x'], node1['y'] - node2['y'])
                if dist < 200 and random.random() > 0.3:
                    self.draw.line(
                        [(node1['x'], node1['y']), (node2['x'], node2['y'])],
                        fill=palette[0], width=1
                    )

        # Draw nodes
        for node in nodes:
            x, y, s = node['x'], node['y'], node['size']
            self.draw.ellipse([x - s, y - s, x + s, y + s], fill=palette[1])

    def _pure_absence(self):
        """Extreme minimalism - almost nothing"""
        palette = self._get_palette(['#ffffff', '#cccccc'])

        # Very subtle gradient
        for r in range(self.size // 2, 0, -20):
            gray = int(10 + (r / (self.size // 2)) * 3)
            color = f'#{gray:02x}{gray:02x}{gray + 2:02x}'
            cx, cy = self.size // 2, self.size // 2
            self.draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)

        # Maybe one tiny element
        if random.random() > 0.5:
            x = self.size * (0.3 + random.random() * 0.4)
            y = self.size * (0.3 + random.random() * 0.4)
            r = 2 + random.random() * 3
            self.draw.ellipse([x - r, y - r, x + r, y + r], fill=palette[0])

    def _spiral_dynamics(self):
        """Spiral and helix patterns"""
        palette = self._get_palette(['#ff6b6b', '#ffd93d', '#ff9f43', '#ee5a24'])
        center_x, center_y = self.size / 2, self.size / 2
        num_spirals = int(2 + self.complexity * 3)

        for s in range(num_spirals):
            start_angle = (s / num_spirals) * math.pi * 2
            direction = 1 if random.random() > 0.5 else -1
            color = palette[s % len(palette)]
            width = int(2 + random.random() * 3)

            points = []
            for i in range(500):
                t = i / 500
                angle = start_angle + t * math.pi * 8 * direction
                radius = t * self.size * 0.45
                x = center_x + math.cos(angle) * radius
                y = center_y + math.sin(angle) * radius
                points.append((x, y))

            if len(points) > 1:
                self.draw.line(points, fill=color, width=width)


# Test the engine
if __name__ == '__main__':
    engine = ArtEngine()
    styles = [
        'geometric_minimalist', 'organic_flow', 'void_exploration',
        'spectral_fragmentation', 'recursive_patterns'
    ]

    for style in styles:
        data = engine.generate(style, seed=42)
        print(f'{style}: Generated {len(data)} bytes of base64 data')
