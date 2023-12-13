import { DynamicTimePipe } from './dynamic-time.pipe';

describe('DynamicTimePipe', () => {
  it('create an instance', () => {
    const pipe = new DynamicTimePipe();
    expect(pipe).toBeTruthy();
  });
});
